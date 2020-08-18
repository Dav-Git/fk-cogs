import discord
from redbot.core import commands


class PaidFeatures(commands.Cog):
    async def red_delete_data_for_user(self, *, requester, user_id):
        pass  # This cog stores no EUD

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        # Welcome to YT-Members
        if before.guild.get_role(699653447561117697) in after.roles:
            if not before.guild.get_role(699653447561117697) in before.roles:
                await after.guild.get_channel(697117977308430356).send(
                    f"Welcome to the YouTube channel members chat {after.mention}!"
                )
        # Welcome to Nitro boosters
        if before.guild.get_role(586310188135481375) in after.roles:
            if not before.guild.get_role(586310188135481375) in before.roles:
                await after.guild.get_channel(699766264784093255).send(
                    f"Welcome to the Nitro-Booster chat {after.mention}!"
                )
