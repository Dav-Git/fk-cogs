from redbot.core import checks, commands
import discord
from typing import Optional


class FKCom(commands.Cog):
    @commands.command()
    @checks.mod()
    async def rp(self, ctx, user: Optional[discord.User]):
        """Blanket warn message for rp questions"""
        await ctx.send(
            "Hey{}, it seems like you have asked a question about ARP (Aspirant Gaming). We are not affiliated with ARP at all and sadly can not provide any information to you. To receive an answer to your question, try {} or the Aspirant Gaming discord server.".format(
                " " + user.mention if user != None else "\u200b",
                ctx.guild.get_channel(478917077705555970).mention,
            )
        )

    @commands.command()
    @checks.mod()
    async def claw(self, ctx, user: discord.Member):
        """``[Member]`` | Puts a member into #contact-claws."""
        roles = {
            "fireteam": ctx.guild.get_role(634692203582717990),
            "burning": ctx.guild.get_role(489455280266936321),
            "contact": ctx.guild.get_role(483212257237401621),
        }
        try:
            if roles["fireteam"] in user.roles:
                await user.remove_roles(roles["fireteam"], reason="Contact claws assigned.")
            elif roles["burning"] in user.roles:
                await user.remove_roles(roles["burning"], reason="Contact claws assigned.")
            await user.add_roles(roles["contact"], reason="Contact claws assigned.")
            await ctx.guild.get_channel(350726339327950859).send(
                f"{user.name} has been put into {ctx.guild.get_channel(483213085293936640).mention}."
            )
        except:
            await ctx.send("An error occured.")

    @commands.group(name="return")
    @checks.mod()
    async def return_member(self, ctx):
        """Return a member out of #contact-claws. Use ``fireteam`` or ``burning`` to decide at which level they re-join the conversation."""
        pass

    @return_member.command()
    async def fireteam(self, ctx, user: discord.Member):
        """Return them as a member of the Fireteam"""
        if ctx.guild.get_role(483212257237401621) in user.roles:
            await user.remove_roles(
                ctx.guild.get_role(483212257237401621), reason="Returned from Contact claws."
            )
            await user.add_roles(
                ctx.guild.get_role(634692203582717990), reason="Returned from Contact claws."
            )
            await ctx.guild.get_channel(350726339327950859).send(
                f"{user.name} has been returned from {ctx.guild.get_channel(483213085293936640).mention}."
            )

    @return_member.command()
    async def burning(self, ctx, user: discord.Member):
        """Return them as a Burning Bright"""
        if ctx.guild.get_role(483212257237401621) in user.roles:
            await user.remove_roles(
                ctx.guild.get_role(483212257237401621), reason="Returned from Contact claws."
            )
            await user.add_roles(
                ctx.guild.get_role(489455280266936321), reason="Returned from Contact claws."
            )
            await ctx.guild.get_channel(350726339327950859).send(
                f"{user.name} has been returned from {ctx.guild.get_channel(483213085293936640).mention}."
            )

    @commands.command()
    @checks.mod()
    async def bot(self, ctx):
        """If someone requests a bot is put in... run this."""
        await ctx.send(
            f"In an effort to keep confusion and management requirements at a minimum we have opted to be a one-bot-server. This means that we will not be adding any other bot besides {ctx.bot.user.mention}. If you would like to request some sort of functionality please describe exactly what you want to see in {ctx.guild.get_channel(340124332111953942)} and we will check if it something we can implement."
        )
