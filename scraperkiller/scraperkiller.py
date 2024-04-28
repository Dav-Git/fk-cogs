from typing import List
import discord
import aiohttp
import logging
from discord.ext import tasks
from redbot.core import commands, Config

log = logging.getLogger(__name__)

class ScraperKiller(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=102825042024,force_registration=True)
        default={"banned":[]}
        self.config.register_global(**default)
        self.ban_scrapers.start()

    def cog_unload(self):
        self.ban_scrapers.cancel()

    async def red_delete_data_for_user(self, *, requester, user_id):
        pass  # This cog stores no EUD

    @tasks.loop(hours=24)
    async def ban_scrapers(self):
        data:List[str] = []
        guild:discord.Guild = self.bot.get_guild(332834024831582210)
        banned:List[str] = await self.config.banned()
        async with aiohttp.ClientSession() as session:
            async with session.get("https://kickthespy.pet/ids") as result:
                data = await result.json()
        if not data:
            log.warn("No banlist retrieved from https://kickthespy.pet/ids")
        else:
            for uid in data:
                if uid in banned:
                    continue
                user:discord.Object = discord.Object(id=int(uid))
                try:
                    await guild.ban(user,reason="Autoban. Listed as User-Scraper")
                    banned.append(uid)
                except Exception as e:
                    log.error(e)
            await self.config.banned.set(banned)