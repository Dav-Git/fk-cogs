from redbot.core import commands


class PrivateVcDeleter(commands.Cog):
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 785086951811186688:
            try:
                await message.delete()
            except:
                pass
