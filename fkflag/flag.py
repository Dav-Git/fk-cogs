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
        default_guild = {"days": 31, "flags": {}}

        self.config.register_global(**default_global)
        self.config.register_guild(**default_guild)

    @staticmethod
    def _flag_template():
        return {"reason": "", "expireyear": 0, "expiremonth": 0, "expireday": 0, "author": None}

    @commands.guild_only()
    @checks.mod_or_permissions(manage_roles=True)
    @commands.command()
    async def flag(self, ctx: commands.Context, member: discord.Member, *, reason):
        """Flag a member"""
        guild = ctx.guild
        if ctx.author == member:
            await ctx.send("Fuck you cunt! <3")
            return
        elif len(reason) > 500:
            await ctx.send("**No u.**\n\nKeep it below 500 chars.")
            return

        flag = self._flag_template()

        flag["reason"] = reason
        flag["author"] = f"{ctx.author.name}#{ctx.author.discriminator}"
        flag["date"] = datetime.utcnow().strftime("%a, %d %b %Y")

        async with self.config.guild(guild).flags() as flags:
            if str(member.id) not in flags:
                flags[str(member.id)] = []
            flags[str(member.id)].append(flag)

        outembed = await self._list_flags(member)

        if outembed:
            for embed in outembed:
                await ctx.send(embed=embed)
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
            for embed in outembed:
                await ctx.send(embed=embed)
        else:
            await ctx.send("This member has no flags!")

    @commands.admin()
    @commands.command()
    async def delflag(self, ctx, member: discord.Member, text: str):
        """Deletes a flag. \n`text` needs to be the FULL flag text."""
        async with self.config.guild(ctx.guild).flags() as allflags:
            flags = allflags[member.id]
            print(flags)
            i = 0
            for flag in flags:
                await ctx.send(f"Found flag {flag}")
                if flag["reason"] == text:
                    del allflags[member.id][i]
                    await ctx.guild.get_channel(360478963115491328).send(
                        f"{ctx.author.mention} deleted a flag for {member.display_name}({member.id})."
                    )
                    embed = discord.Embed(title=f"Flag for {member.name}#{member.discriminator}")
                    try:
                        flag["date"]
                    except KeyError:
                        flag["date"] = "N/A"
                    try:
                        flag["author"]
                    except KeyError:
                        flag["author"] = "N/A"
                    try:
                        embed.add_field(
                            name=f"\u200b\u200b",
                            value=f"**Reason: {flag['reason']}**\nAuthor: {flag['author']}\nDate: {flag['date']}",
                            inline=False,
                        )
                    except KeyError:
                        embed.add_field(
                            name=f"\u200b\u200b",
                            value=f"**Reason: {flag['reason']}**\nAn error occurred while fetching metadata.",
                            inline=True,
                        )
                    await ctx.guild.get_channel(360478963115491328).send(embed=embed)
                    await ctx.tick()
                    return
                i += 1
        await ctx.send("Specified flag not found.")

    async def _list_flags(self, member: discord.Member):
        """Returns a pretty embed of flags on a member"""
        done = False
        flags = await self.config.guild(member.guild).flags.get_raw(str(member.id), default=[])
        flagno = len(flags)
        embedlist = []

        while not done:
            if len(flags) == 0 and flagno != 0:
                break
            embed = discord.Embed(
                title="Flags for " + member.display_name,
                description="User has {} active flags".format(flagno),
                color=0x804040,
            )
            if flagno == 0:
                done = True
                break
            counter = 0
            flags_to_remove = []
            for flag in flags:
                if counter == 16:
                    break
                flags_to_remove.append(
                    flag
                )  # Do this here so past modifications don't screw with it.
                try:
                    flag["date"]
                except KeyError:
                    flag["date"] = "N/A"
                try:
                    flag["author"]
                except KeyError:
                    flag["author"] = "N/A"
                try:
                    embed.add_field(
                        name=f"\u200b\u200b",
                        value=f"**Reason: {flag['reason']}**\nAuthor: {flag['author']}\nDate: {flag['date']}",
                        inline=False,
                    )
                except KeyError:
                    embed.add_field(
                        name=f"\u200b\u200b",
                        value=f"**Reason: {flag['reason']}**\nAn error occurred while fetching metadata.",
                        inline=True,
                    )
                counter += 1
                if len(flags) == 0:
                    done = True
                    break

            for flag in flags_to_remove:
                flags.remove(flag)

            embed.set_thumbnail(url=member.avatar_url)
            embedlist.append(embed)

        return embedlist

    async def _check_flags(self, guild: discord.Guild):
        """Updates and removes expired flags"""
        return
