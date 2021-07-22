import asyncio
import time

import discord
from discord.ext import tasks
from redbot.core import Config, commands


def isStaff():
    async def predicate(ctx) -> bool:
        staffroles = [
            450253903209168906,
            530016413616963591,
            332835206493110272,
            332834961407213568,
            344440746264231936,
        ]
        userroles = [r.id for r in ctx.author.roles]
        if any(role in userroles for role in staffroles):
            return True
        else:
            return False

    return commands.check(predicate)


class FKBday(commands.Cog):
    def __init__(self, bot):
        self.config = Config.get_conf(self, identifier=959)
        default_guild = {"bdays": {}}
        self.config.register_guild(**default_guild)
        self.bot = bot

    @tasks.loop(hours=1)
    async def bdayremover(self):
        todel = []
        async with self.config.guild_from_id(332834024831582210).bdays as bdays:
            for date in bdays:
                if int(time.time()) > date:
                    guild = self.bot.get_guild(332834024831582210)
                    await guild.get_member(bdays[date]).remove_roles(
                        guild.get_role(657943577065947157), reason="Their birthday is over!"
                    )
                    todel.append(date)
        await self.config.guild_from_id(332834024831582210).bdays()
        for d in todel:
            del bdays[d]
        await self.config.guild_from_id(332834024831582210).bdays.set(bdays)

    @isStaff()
    @commands.command(aliases=["birthday", "bd"])
    async def bday(self, ctx, *, user: discord.Member):
        """Says happy birthday to a user"""
        await ctx.send("Happy Birthday, **{0}**! :tada:".format(user.display_name))
        await user.add_roles(ctx.guild.get_role(657943577065947157), reason="It's their birthday!")
        async with self.config.guild(ctx.guild).bdays() as bdays:
            # get unix timestamp
            end_timestamp = int(time.time()) + 86400
            bdays[end_timestamp] = user.id
