from random import choice
import contextlib
import asyncio
import discord
from discord.ext import tasks
from redbot.core import commands
from redbot.core.utils import AsyncIter
from collections import defaultdict


class LukasStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._user_count = 0
        self.user_task = asyncio.create_task(self._get_user_count())
        self._update_presence.start()

    def cog_unload(self):
        self.user_task.cancel()
        self._update_presence.cancel()

    @tasks.loop(minutes=2)
    async def _update_presence(self):
        users = self._user_count
        guilds = len(self.bot.guilds)
        strings = [
            " .payday to earn some diamonds",
            " .help for all commands",
            f" {users} users and {guilds} servers",
            " you",
        ]
        await self.bot.change_presence(
            activity=discord.Activity(name=choice(strings), type=discord.ActivityType.watching)
        )

    async def _get_user_count(self):
        await self.bot.wait_until_ready()
        with contextlib.suppress(asyncio.CancelledError):
            self._user_count = len(self.bot.users)
            while True:
                temp_data = defaultdict(set)
                async for s in AsyncIter(self.bot.guilds):
                    if s.unavailable:
                        continue
                    async for m in AsyncIter(s.members):
                        temp_data["Unique Users"].add(m.id)
                self._user_count = len(temp_data["Unique Users"])
                await asyncio.sleep(60)
