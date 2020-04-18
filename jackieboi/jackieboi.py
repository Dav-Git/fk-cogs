from redbot.core import commands, checks
import discord
from typing import Optional


class JackieBoi(commands.Cog):
    """JackieCog"""

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
            await whoever_the_fuck_needs_changed.edit(nick="change", reason=reason)
        except discord.errors.Forbidden:
            await ctx.send("Missing permissions.")
