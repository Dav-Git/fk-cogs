from redbot.core import commands
from discord import Embed
from datetime import datetime


class JackWelcome(commands.Cog):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 497097726400528394:
            emoji = "{WAVING HAND SIGN}"
            em = Embed(
                title=f"{member.mention} joined the guild.",
                description=f"{emoji}  -  Welcome to **Aurora** {member.name}, we hope you enjoy your stay! We'd appreciate it if you read the rules, if you want some cool and shiny roles check out {member.guild.get_channel(643864880285351966).mention}.",
                timestamp=datetime.utcnow(),
                thumbnail="https://cdn.discordapp.com/icons/497097726400528394/00453191715921c03ca41dbe8b1a0569.png?size=128",
            )
            em.set_image(url="https://tenor.com/view/welcome-gif-10939070")
            await member.guild.get_channel(718798993852727317).send(embed=em)
