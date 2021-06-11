import discord
from discord.ext import tasks
from redbot.core import commands


class RaptorHi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 749863506228150383:
            await self.bot.change_presence(
                status=discord.Status.dnd,
                activity=discord.Activity(
                    type=discord.ActivityType.watching,
                    name=f"Hi {member.display_name}, Welcome to the raptor pen.",
                ),
            )

    @tasks.loop(minutes=15)
    async def update_member_count(self):
        await self.bot.change_presence(
            status=discord.Status.online,
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name=f"all {self.bot.get_guild(749863506228150383).member_count} members of the raptor pen.",
            ),
        )
