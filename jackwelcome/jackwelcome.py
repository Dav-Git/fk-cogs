from redbot.core import commands
from discord import Embed, Color
from datetime import datetime


class JackWelcome(commands.Cog):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 497097726400528394:
            em = Embed(
                title=f"{member.name} joined the guild.",
                description=f":wave:  -  Welcome to **Aurora** {member.mention}, we hope you enjoy your stay! We'd appreciate it if you read the rules, if you want some cool and shiny roles check out {member.guild.get_channel(643864880285351966).mention}.",
                timestamp=datetime.utcnow(),
                color=Color.from_rgb(34, 139, 34),
            )
            em.set_author(
                name="Aurora",
                icon_url="https://cdn.discordapp.com/icons/497097726400528394/00453191715921c03ca41dbe8b1a0569.png?size=128",
            )
            em.set_image(
                url="https://cdn.discordapp.com/attachments/663351785293086720/718843908729077830/Aurora_Welcome_Banner.jpg"
            )
            await member.guild.get_channel(718798993852727317).send(embed=em)

    @commands.Cog.listener()
    async def on_member_leave(self, member):
        if member.guild.id == 497097726400528394:
            em = Embed(
                title=f"{member.name} left the guild.",
                description=f":wave:  -  Sorry to see you go {member.name}#{member.discriminator}, return again soon!",
                timestamp=datetime.utcnow(),
                color=Color.dark_red(),
            )
            em.set_author(
                name="Aurora",
                icon_url="https://cdn.discordapp.com/icons/497097726400528394/00453191715921c03ca41dbe8b1a0569.png?size=128",
            )
            em.set_image(
                url="https://cdn.discordapp.com/attachments/663351785293086720/718843903561695282/Aurora_Farewell_Banner.jpg"
            )
            await member.guild.get_channel(718798993852727317).send(embed=em)
