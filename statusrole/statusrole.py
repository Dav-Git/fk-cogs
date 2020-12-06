from redbot.core import commands, Config, checks
import discord


class Statusrole(commands.Cog):
    def __init__(self):
        self.config = Config.get_conf(self, 1234, force_registration=True)
        default_guild = {"text_to_role_id": {}}
        self.config.register_guild(**default_guild)
        self.text_to_role = {}

    async def initialize(self, bot):
        await bot.wait_until_red_ready()
        for guild in bot.guilds:
            await self._update_cache(guild)

    @commands.Cog.listener()
    async def on_member_update(self, before, member: discord.Member):
        if member.activity:
            if (
                member.activity.type == discord.ActivityType.custom
                or member.activity.type == discord.ActivityType.playing
            ):
                try:
                    for text in self.text_to_role[member.guild]:
                        if text in member.activity.name:
                            role = self.text_to_role[member.guild][text]
                            if not role in member.roles:
                                await member.add_roles(role)
                        else:
                            await self._maybe_remove_role(member)
                except KeyError:
                    pass
                except TypeError:
                    pass
            else:
                await self._maybe_remove_role(member)
        else:
            await self._maybe_remove_role(member)

    @commands.group()
    async def statusrole(self, ctx):
        """Statusrole commands."""
        pass

    @checks.admin()
    @statusrole.command()
    async def add(self, ctx, role: discord.Role, *, text: str):
        """Add a text to role relation."""
        if len(text) > 128:
            return await ctx.send("A status message can not be that long.")
        async with self.config.guild(ctx.guild).text_to_role_id() as text_to_role_id:
            text_to_role_id[text] = role.id
        await self._update_cache(ctx.guild)
        await ctx.send(
            f"Users with ``{text}`` in their status will now get the ``{role.name}`` role."
        )

    @checks.admin()
    @statusrole.command()
    async def remove(self, ctx, *, text: str):
        """Remove a text to role relation."""
        try:
            async with self.config.guild(ctx.guild).text_to_role_id() as text_to_role_id:
                del text_to_role_id[text]
            await self._update_cache(ctx.guild)
            await ctx.send(
                f"Statusrole removed.\nTo remove the role from all members run ``{ctx.clean_prefix}statusrole purge <role>``"
            )
        except KeyError:
            await ctx.send("This text is not known as a statusrole.")

    @checks.admin()
    @statusrole.command(name="list")
    async def list_statusroles(self, ctx):
        """List all text to role relations."""
        data = self.text_to_role[ctx.guild]
        for key in data:
            await ctx.send(
                f"Members with the ``{key}`` status will get the ``{data[key].name}`` role."
            )

    @checks.admin()
    @statusrole.command()
    async def purge(self, ctx, role: discord.Role):
        """Remove a role from all your members."""
        async with ctx.typing():
            for member in ctx.guild.members:
                if role in member.roles:
                    try:
                        await member.remove_roles(role, reason="Statusrole purge")
                    except:
                        pass
        await ctx.send("Role purged.")

    async def _update_cache(self, guild):
        text_to_role_id = await self.config.guild(guild).text_to_role_id()
        text_to_role = {}
        for text in text_to_role_id:
            text_to_role[text] = guild.get_role(text_to_role_id[text])
        self.text_to_role[guild] = text_to_role

    async def _maybe_remove_role(self, member):
        try:  # Make sure this doesn't error when no info about the guild was saved.
            self.text_to_role[member.guild].values()
        except KeyError:
            return
        if member.activity:
            if member.activity.name in self.text_to_role[member.guild]:
                return
        for role in member.roles:
            if role in self.text_to_role[member.guild].values():
                await member.remove_roles(role)