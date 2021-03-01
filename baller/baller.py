from redbot.core import commands


class Baller(commands.Cog):
    @commands.Cog.listener()
    async def on_command(self, ctx):
        if ctx.command == ctx.bot.get_command("8ball"):
            await ctx.send(f"{ctx.author.mention} asked: {ctx.command.args}")
