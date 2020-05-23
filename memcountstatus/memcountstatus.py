import discord
from redbot.core import commands, checks
from discord.ext import tasks


class MemCountStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._memcount_to_status.start()

    def cog_unload(self):
        self._memcount_to_status.cancel()

    @tasks.loop(minutes=5)
    async def _memcount_to_status(self):
        await self.bot.wait_until_ready()
        guild = self.bot.get_guild(332834024831582210)
        mc = len(guild.members)
        activity = discord.Activity(
            name=f" over {mc} members.", type=discord.ActivityType.watching
        )
        await self.bot.change_presence(activity=activity)

    @checks.admin()
    @commands.command()
    async def mcs(self, ctx):
        await self._memcount_to_status()
