from redbot.core import commands, Config, checks
import discord


class Statusrole(commands.Cog):
    def __init__(self):
        self.config = Config.get_conf(self, 1234, force_registration=True)
        default_guild = {"text_to_role_id": {}}
        self.config.register_guild(**default_guild)
        self.text_to_role = {}

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

    async def _update_cache(self, guild):
        text_to_role_id = await self.config.guild(guild).text_to_role_id()
        text_to_role = {}
        for text in text_to_role_id:
            text_to_role[text] = guild.get_role(text_to_role_id[text])
        self.text_to_role = text_to_role
