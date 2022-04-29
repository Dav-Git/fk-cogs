import discord
from redbot.core import commands


class RaptorLivePing(commands.Cog):
    """Ping when Raptor goes live"""

    @commands.Cog.listener()
    async def on_message_without_command(self, message):
        """Ping when Raptor goes live"""
        if message.channel.id == 750713006098481193:
            if not 966353849969410169 in message.role_mentions:
                await message.channel.send(
                    message.guild.get_role(966353849969410169).mention,
                    allowed_mentions=discord.AllowedMentions(roles=True),
                )
