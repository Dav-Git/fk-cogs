import discord
from redbot.core import commands, checks, Config
from discord.ext import tasks
from random import choice
from datetime import datetime, timedelta
import asyncio


class MemCountStatus(commands.Cog):
    async def red_delete_data_for_user(self, *, requester, user_id):
        pass  # This cog stores no EUD

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=234524052020, force_registration=True)
        default = {"statuses": ["\u200b", "\u200b\u200b", ("watching", "you.")], "memdiff": 0}
        self.config.register_global(**default)
        self._update_status.start()
        self._clear_memcount.start()

    def cog_unload(self):
        self._update_status.cancel()
        self._clear_memcount.cancel()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 332834024831582210:
            await self.config.memdiff.set(await self.config.memdiff() + 1)
            await self._memdiff_to_status()

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id == 332834024831582210:
            await self.config.memdiff.set(await self.config.memdiff() - 1)
            await self._memdiff_to_status()

    @tasks.loop(minutes=5)
    async def _update_status(self):
        the_chosen_one = choice(await self.config.statuses())
        if the_chosen_one == "\u200b":
            await self._memcount_to_status()
        elif the_chosen_one == "\u200b\u200b":
            await self._memdiff_to_status()
        else:
            t = getattr(discord.ActivityType, the_chosen_one[0], False)
            s = getattr(discord.Status, choice(["online", "idle", "dnd"]), False)
            activity = discord.Activity(name=the_chosen_one[1], type=t)
            await self.bot.change_presence(status=s, activity=activity)

    @tasks.loop(minutes=10)
    async def _clear_memcount(self):
        now = datetime.utcnow()
        midnight = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
        await asyncio.sleep((midnight - now).total_seconds())
        await self.config.memdiff.set(0)

    async def _memcount_to_status(self):
        guild = self.bot.get_guild(332834024831582210)
        mc = len(guild.members)
        activity = discord.Activity(
            name=f" over {mc} members.", type=discord.ActivityType.watching
        )
        await self.bot.change_presence(activity=activity)

    async def _memdiff_to_status(self):
        mc = await self.config.memdiff()
        if mc == 0:
            text = "No new members yet today."
        elif mc > 0:
            text = f"+{mc} new members."
        elif mc < 0:
            text = f"{mc} members today."
        activity = discord.Activity(name=text, type=discord.ActivityType.watching)
        await self.bot.change_presence(status=discord.Status.idle, activity=activity)

    @checks.admin()
    @commands.command()
    async def mcs(self, ctx):
        await self._memcount_to_status()
        await ctx.send("It is done.", delete_after=10)

    @checks.admin()
    @commands.command()
    async def forcenextstatus(self, ctx):
        self._update_status.restart()
        await ctx.send("I have chosen a new random status from the pool.", delete_after=10)

    @checks.admin()
    @commands.command()
    async def addstatus(self, ctx, status_type: int, *, text: str):
        """**Types:**\n0 = ``Playing``\n1 = ``Watching``\n2 = ``Listening``"""
        if status_type == 0:
            st = "playing"
        elif status_type == 1:
            st = "watching"
        elif status_type == 2:
            st = "listening"
        else:
            st = None
        if st:
            async with self.config.statuses() as statuses:
                statuses.append((st, text))
            await ctx.send(f"``{st} {text}`` added.")

    @checks.admin()
    @commands.command()
    async def liststatus(self, ctx):
        statuses = await self.config.statuses()
        count = 0
        divcount = 0
        text = []
        for i in statuses:
            if i == "\u200b":
                text.append(f"**{count}** | Membercount")
            elif i == "\u200b\u200b":
                text.append(f"**{count}** | Memberdifference per day")
            else:
                text.append(f"**{count}** | ``{i[0]} {i[1]}``")
            count += 1
            divcount += 1
            if divcount % 5 == 0:
                await ctx.send("\n".join(text))
                text = []
                divcount = 0
        if not divcount == 0:
            await ctx.send("\n".join(text))

    @checks.admin()
    @commands.command()
    async def deletestatus(self, ctx, number: int):
        async with self.config.statuses() as statuses:
            statuses.remove(statuses[number])
        await ctx.send("It has been done.")
