import discord
from redbot.core import commands
from discord.ext import tasks


class DungeonKick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._kick_dungeon_members.start()

    def cog_unload(self):
        self._kick_dungeon_members.cancel()

    @tasks.loop(hours=24)
    async def _kick_dungeon_members(self):
        await self.bot.wait_until_red_ready()
        for m in self.bot.get_guild(332834024831582210).get_role(718099883692785747).members:
            await m.kick(reason="Member got lost in the dungeon...")
