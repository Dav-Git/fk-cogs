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
            if member in race.players[ctx.guild.id]:
                return await ctx.send(
                    f"{member.display_name} is already racing. Don't force them to race twice you meanie."
                )
            elif len(race.players[ctx.guild.id]) >= 14:
                return await ctx.send(
                    "Yo yo yo, only 14 people fit on the track. You can't squish them to fit more..."
                )
            else:
                race.players[ctx.guild.id].append(member)
                await ctx.send(f"Alex forced {member.display_name} to race.")
        else:
            await ctx.send(f"There is no race ongoing. Start one first.")
