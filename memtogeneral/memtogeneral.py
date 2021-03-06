from redbot.core import commands, checks
from discord.ext import tasks


class MemToGeneral(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._memcount_to_general.start()

    def cog_unload(self):
        self._memcount_to_general.cancel()

    @tasks.loop(minutes=5)
    async def _memcount_to_general(self):
        await self.bot.get_guild(497097726400528394).get_channel(497101356646006784).edit(
            topic=f"Invite link is: https://discord.gg/zbJtTxe \nCurrently at {len(self.bot.get_guild(497097726400528394).members)} members."
        )

    @commands.command()
    @checks.is_owner()
    async def memtogeneral(self, ctx):
        await self.bot.get_guild(497097726400528394).get_channel(497101356646006784).edit(
            topic=f"Invite link is: https://discord.gg/zbJtTxe \nCurrently at {len(self.bot.get_guild(497097726400528394).members)} members."
        )
