from redbot.core import commands
import discord


class NickNamer(commands.Cog):
    """ForceNick"""

    @commands.command()
    async def nick(self, ctx, user: discord.Member, *, name):
        """Change a user's nickname"""
        try:
            await user.edit(nick=name)
            await user.send(f"Your nickname on ``{ctx.guild.name}`` has been changed.")
        except discord.errors.Forbidden:
            await ctx.send("Missing permissions.")
