from redbot.core import commands, checks, modlog
import discord
from typing import Optional
from datetime import datetime


class JackieBoi(commands.Cog):
    """JackieCog"""

    async def __init__(self, bot):
        self.bot = bot

    async def intialize(self):
        await self.register_casetypes()

    @staticmethod
    async def register_casetypes():
        forcechange_case = {
            "name": "forcechange",
            "default_setting": True,
            "image": ":pencil2:",
            "case_str": "Nickname force-changed",
        }
        await modlog.register_casetype(**forcechange_case)

    @checks.mod()
    @commands.command()
    async def forcenick(
        self, ctx, whoever_the_fuck_needs_changed: discord.Member, *, reason: Optional[str]
    ):
        if not reason:
            reason = f"Nickname force-changed by {ctx.author.mention}"
        else:
            reason = f'"{reason}" requested by {ctx.author.mention}.'
        try:
            await whoever_the_fuck_needs_changed.edit(nick="change")
            await modlog.create_case(
                self.bot,
                ctx.guild,
                datetime.now(),
                "forcechange",
                whoever_the_fuck_needs_changed,
                moderator=ctx.author,
                reason=reason,
                channel=ctx.channel,
            )
        except discord.errors.Forbidden:
            await ctx.send("Missing permissions.")
