from datetime import datetime, date, timedelta

import discord
from redbot.core import Config, checks, commands
from redbot.core.bot import Red
from redbot.core.commands import Cog
from redbot.core.utils.chat_formatting import pagify


class Flag(Cog):
    """
    Set expiring flags on members
    """

    async def red_delete_data_for_user(self, *, requester, user_id):
        if requester == "owner" or requester == "discord_deleted_user":
            for guild_id in await self.config.guild.all():
                await self.config.guild_from_id(guild_id).flags.set_raw(str(user_id), value=[])

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=9811198108111121, force_registration=True)
        default_global = {}
        default_guild = {"days": 31, "dm": True, "flags": {}}

        self.config.register_global(**default_global)
        self.config.register_guild(**default_guild)

    @checks.mod_or_permissions(manage_roles=True)
    @commands.guild_only()
    @commands.group()
    async def flagset(self, ctx: commands.Context):
        """
        My custom cog
       
        Extra information goes here
        """
        if ctx.invoked_subcommand is None:
            pass

    @flagset.command(name="dm")
    async def flagset_dm(self, ctx: commands.Context):
        """Toggles DM-ing the flags"""

        dm = await self.config.guild(ctx.guild).dm()
        await self.config.guild(ctx.guild).dm.set(not dm)

        await ctx.send("DM-ing members when they get a flag is now set to **{}**".format(not dm))

    @staticmethod
    def _flag_template():
        return {"reason": "", "expireyear": 0, "expiremonth": 0, "expireday": 0, "author": None}

    @commands.guild_only()
    @checks.mod_or_permissions(manage_roles=True)
    @commands.command()
    async def flag(self, ctx: commands.Context, member: discord.Member, *, reason):
        """Flag a member"""
        guild = ctx.guild
        if ctx.author=member:
            await ctx.send("Fuck you!")
            return

        flag = self._flag_template()

        flag["reason"] = reason
        flag["author"] = f"{ctx.author.name}#{ctx.author.discriminator}"
        flag["date"] = datetime.utcnow().strftime('%a, %d %b %Y')

        async with self.config.guild(guild).flags() as flags:
            if str(member.id) not in flags:
                flags[str(member.id)] = []
            flags[str(member.id)].append(flag)

        outembed = await self._list_flags(member)

        if outembed:
            await ctx.send(embed=outembed)
            if await self.config.guild(guild).dm():
                try:
                    await member.send(embed=outembed)
                except discord.Forbidden:
                    await ctx.send("DM-ing user failed")
        else:
            await ctx.send("This member has no flags.. somehow..")

    @commands.guild_only()
    @commands.command(aliases=["flaglist"])
    async def listflag(self, ctx: commands.Context, member: discord.Member):
        """Lists flags for a member"""
        server = ctx.guild
        await self._check_flags(server)

        outembed = await self._list_flags(member)

        if outembed:
            await ctx.send(embed=outembed)
        else:
            await ctx.send("This member has no flags!")

    @commands.guild_only()
    @commands.command(aliases=["flagall"])
    async def allflag(self, ctx: commands.Context):
        """Lists all flags for the server"""
        guild = ctx.guild
        await self._check_flags(guild)
        out = "All flags for {}\n".format(ctx.guild.name)

        flags = await self.config.guild(guild).flags()
        flag_d = {}
        for memberid, flag_data in flags.items():
            if len(flag_data) > 0:
                member = guild.get_member(int(memberid))
                flag_d[member.display_name + member.discriminator] = len(flag_data)

        for display_name, flag_count in sorted(flag_d.items()):
            out += "{} - **{}** flags".format(display_name, flag_count)

        for page in pagify(out):
            await ctx.send(page)

    async def _list_flags(self, member: discord.Member):
        """Returns a pretty embed of flags on a member"""
        flags = await self.config.guild(member.guild).flags.get_raw(str(member.id), default=[])

        embed = discord.Embed(
            title="Flags for " + member.display_name,
            description="User has {} active flags".format(len(flags)),
            color=0x804040,
        )
        for flag in flags:
            try:
                flag["date"]
            except KeyError:
                flag["date"]="N/A"
            try:
                flag["author"]
            except KeyError:
                flag["author"]="N/A"
            try:
                embed.add_field(
                    name=f"Reason: {flag['reason']}",
                    value=f"Author: {flag['author']}\nDate: {flag['date']}",
                    inline=True,
                )
            except KeyError:
                embed.add_field(
                    name=f"Reason: {flag['reason']}", value="An error occurred whirl fetching metadata.", inline=True,
                )

        embed.set_thumbnail(url=member.avatar_url)

        return embed

    async def _check_flags(self, guild: discord.Guild):
        """Updates and removes expired flags"""
        return
