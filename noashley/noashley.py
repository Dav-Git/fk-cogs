from redbot.core import commands


class NoAshley(commands.Cog):
    def __init__(self):
        self.deleted = False

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        if channel.name == "mods":
            channel = await channel.guild.get_channel(591466874458472448).create_text_channel(
                "mods"
            )
            if self.deleted:
                await channel.send("You shall not get rid of me!")
            else:
                self.deleted = True
