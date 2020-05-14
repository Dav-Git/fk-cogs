import discord
from redbot.core import commands


class DaCow(commands.Cog):
    """Manages the cow"""

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        # Moo
        if after.id == 332834024831582210:
            if not before.overwrites == after.overwrites:
                overwrites = before.overwrites
                for key in overwrites:
                    if isinstance(key, discord.Member):
                        await key.remove_roles(
                            after.guild.get_role(707949167338586123), reason="No mo moo"
                        )
                overwrites = after.overwrites
                for key in overwrites:
                    if isinstance(key, discord.Member):
                        await key.add_roles(after.guild.get_role(707949167338586123), reason="moo")
