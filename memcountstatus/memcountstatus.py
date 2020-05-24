import discord
from redbot.core import commands, checks, Config
from discord.ext import tasks
from random import choice


class MemCountStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=234524052020, force_registration=True)
        default = {"statuses": ["\u200b", ("watching", "you.")]}
        self.config.register_global(**default)
        self._update_status.start()

    def cog_unload(self):
        self._update_status.cancel()

    @tasks.loop(minutes=3)
    async def _update_status(self):
        async with self.config.statuses() as statuses:
            the_chosen_one = choice(statuses)
            if the_chosen_one == "\u200b":
                await self._memcount_to_status()
            else:
                t = getattr(discord.ActivityType, the_chosen_one[0], False)
                s = getattr(discord.Status, choice(["online", "idle", "dnd"]), False)
                activity = discord.Activity(name=the_chosen_one[1], type=t)
                await self.bot.change_presence(status=s, activity=activity)

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
    async def mcs(self, ctx, mc: bool):
        if mc:
            await self._memcount_to_status()
        else:
            await self._update_status()

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
        for i in statuses:
            if i == "\u200b":
                await ctx.send(f"**{count}** | Membercount")
            else:
                await ctx.send(f"**{count}** | ``{i[0]} {i[1]}``")
            count += 1

    @checks.admin()
    @commands.command()
    async def deletestatus(self, ctx, number: int):
        async with self.config.statuses() as statuses:
            statuses.remove(statuses[number])
        await ctx.send("It has been done.")
