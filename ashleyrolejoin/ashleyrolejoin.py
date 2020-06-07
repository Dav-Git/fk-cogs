import logging
from redbot.core import commands


class AshleyRoleJoin(commands.Cog):
    def __init__(self):
        self.log = logging.getLogger("red.cog.dav-private-cogs.ashleyrolejoin")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 718316599559585843:
            try:
                await member.add_roles(
                    member.guild.get_role(719155457704591361),  # BML
                    member.guild.get_role(719155463165444147),  # Covid
                    member.guild.get_role(719155466533470249),  # LEO
                    member.guild.get_role(719155469591117886),  # Selfies
                    member.guild.get_role(719155568404725791),  # Food
                    member.guild.get_role(719155569168220201),  # Trigger warning
                    reason="New join",
                )
            except Exception as e:
                self.log.exception(e, exc_info=True)
            try:
                await member.send(
                    "Welcome to the ``2020 Mental Health Resource`` discord. \n\nBy default you will be subsribed to all topics in this server. To unsubscribe from one of the topics, visit #self-roles and click twice on the reaction corresponding to the topic you want to unsubscribe from."
                )
            except:
                pass
