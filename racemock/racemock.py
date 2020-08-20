from redbot.core import commands
import discord


def is_amy():
    async def predicate(ctx):
        return ctx.author.id == 716270669725171754

    return commands.check(predicate)


class FakeCTX(discord.Member):
    def __init__(self, author):
        self.author = author


class RaceMock(commands.Cog):
    @is_amy()
    @commands.command()
    async def racemock(self, ctx, member: discord.Member):
        """Allow amy to force people to race"""

        await ctx.bot.get_command("race enter")(FakeCTX(member))
