import discord
from redbot.core import commands


class VCExpand(commands.cog):
    """Expands the VC if staff inside"""

    async def red_delete_data_for_user(self, *, requester, user_id):
        pass  # This cog stores no EUD

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        # Expand VC if more than 3 staff inside
        staffcounter = 0
        if after.channel:
            channelref = after.channel
        elif before.channel:
            channelref = before.channel
        mems = channelref.members
        staffroles = (
            channelref.guild.get_role(530016413616963591),
            channelref.guild.get_role(332835206493110272),
            channelref.guild.get_role(344440746264231936),
            channelref.guild.get_role(332834961407213568),
        )
        for m in mems:
            for r in staffroles:
                if r in m.roles:
                    staffcounter += 1
        if staffcounter > 2 and staffcounter < 6:
            await channelref.edit(user_limit=15, reason="3+ Staff in channel.")
        elif staffcounter > 5:
            await channelref.edit(user_limit=20, reason="6+ Staff in channel.")
        else:
            await channelref.edit(user_limit=10, reason="Fewer than 3 Staff in channel.")
