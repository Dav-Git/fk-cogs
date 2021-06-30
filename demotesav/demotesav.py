import discord
from redbot.core import commands


class DemoteSav(commands.Cog):
    @commands.Cog.listener()
    async def on_member_update(self, member):
        if member.id == 440643588477550592:
            if member.guild.id == 332834024831582210:
                roles = [role.id for role in member.roles]
                if 530016413616963591 in roles:
                    pass
                else:
                    await member.guild.get_channel(465639800406278146).send(
                        "https://cdn.discordapp.com/attachments/332834024831582210/859878777634422784/fedora.png"
                    )
