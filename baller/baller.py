from redbot.core import commands


class Baller(commands.Cog):
    @commands.Cog.listener()
    async def on_command(self, ctx):
        if ctx.message.startswith() == ctx.bot.get_command("8"):
            print("hi")
            await ctx.send(f"{ctx.author.mention} asked: {ctx.command.args}")
