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
    async def claw(self, ctx, user: discord.Member):
        f"""``[Member]`` | Puts a member into {ctx.guild.get_channel(483213085293936640).mention}."""
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

