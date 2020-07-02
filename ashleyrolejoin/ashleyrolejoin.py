import logging
from redbot.core import commands


class AshleyRoleJoin(commands.Cog):
    def __init__(self):
        self.log = logging.getLogger("red.cog.dav-private-cogs.ashleyrolejoin")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 718316599559585843:
            try:
                await member.send(
                    "Welcome to the ``Mental Health Together`` discord. \n\nBy default you will not be subsribed to any topic in this server. To subscribe to one of the topics, visit #self-roles and click on the reaction corresponding to the topic you want to subscribe to."
                )
            except:
                self.log.info(
                    f"{member.name}#{member.discriminator}({member.id}) has their DMs closed."
                )
