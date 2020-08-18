import discord
from redbot.core import commands


class TheDot(commands.Cog):
    """Manage the dot"""

    async def red_delete_data_for_user(self, *, requester, user_id):
        pass  # This cog stores no EUD

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        # Remove burning if dot is present
        if after.guild.get_role(498528746123427851) in after.roles:
            if after.guild.get_role(489455280266936321) in after.roles:
                await after.remove_roles(after.guild.get_role(489455280266936321))
                await after.add_roles(after.guild.get_role(634692203582717990))
