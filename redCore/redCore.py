from redbot.core import commands


class redCore(commands.Cog):
    """Core functions"""

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.id == 428675506947227648 and before.guild.id == 497097726400528394:
            await after.edit(nick="James bond.", reason="No jackieboi!")
