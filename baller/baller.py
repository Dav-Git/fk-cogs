from redbot.core import commands


class Baller(commands.Cog):
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith("-8"):
            await message.channel.send(
                f'{message.author.mention} asked: {message.content.replace("-8","",1).replace("-8ball","",1)}'
            )
