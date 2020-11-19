from redbot.core import commands


class PrivateVcDeleter(commands.Cog):
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 779118031385133126:
            try:
                await message.delete()
            except:
                pass
