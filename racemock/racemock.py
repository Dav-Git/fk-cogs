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
    async def red_delete_data_for_user(self, **kwargs):
        pass

    @is_amy()
    @commands.command()
    async def racemock(self, ctx, member: discord.Member):
        """Allow amy to force people to race"""

        race = ctx.bot.get_cog("Race")
        if race.active:
            race.players.append(member)
            await ctx.send(f"Amy forced {member.display_name} to race.")
        elif member in race.players:
            await ctx.send(
                f"{member.display_name} is already racing. Don't force them to race twice you meanie."
            )
        else:
            await ctx.send(f"There is no race ongoing. Start one first.")
