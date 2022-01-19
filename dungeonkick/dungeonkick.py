from datetime import datetime
import discord
from redbot.core import commands
from discord.ext import tasks


class DungeonKick(commands.Cog):
    async def red_delete_data_for_user(self, *, requester, user_id):
        pass  # This cog stores no EUD

    def __init__(self, bot):
        self.bot = bot
        self._kick_dungeon_members.start()

    def cog_unload(self):
        self._kick_dungeon_members.cancel()

    @tasks.loop(hours=24)
    async def _kick_dungeon_members(self):
        await self.bot.wait_until_red_ready()
        m: discord.Member
        for m in self.bot.get_guild(332834024831582210).get_role(718099883692785747).members:
            time = m.joined_at.timestamp()
            if time > (datetime.now().timestamp() - (86400 * 30)):
                await m.kick(
                    reason=f"Member got lost in the dungeon...\nJoined at: <t:{time}:f> (<t:{time}:R>)"
                )
