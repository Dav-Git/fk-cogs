from redbot.core import commands, checks, modlog
import discord
from typing import Optional
from datetime import datetime


class JackieBoi(commands.Cog):
    """JackieCog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        # Show #no-mic if member in VC
        if after.channel:
            if after.channel.id in [
                497123927605248000,
                708311725803438171,
            ]:
                overwrite = discord.PermissionOverwrite()
                overwrite.send_messages = True
                overwrite.read_messages = True
                await member.guild.get_channel(630729731825991700).set_permissions(
                    member, overwrite=overwrite
                )
            else:
                await member.guild.get_channel(630729731825991700).set_permissions(
                    member, overwrite=None
                )
        else:
            await member.guild.get_channel(630729731825991700).set_permissions(
                member, overwrite=None
            )
