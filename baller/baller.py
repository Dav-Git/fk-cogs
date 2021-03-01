from redbot.core import commands


class Baller(commands.Cog):
    @commands.Cog.listener()
    async def on_message(self, message):
        print("boop")
        if message.startswith("-8"):
            print("hi")
            await message.channel.send(f"{message.author.mention} asked: {message}")
