import discord
from sys import stderr
from redbot.core import commands, checks


class Claw(commands.Cog):
    """Claw cog"""

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
            print(
                f"{ctx.author.name}({ctx.author.id}) clawed {user.name}({user.id}).", file=stderr
            )
        except:
            await ctx.send("An error occured.")
            print(
                f"{ctx.author.name}({ctx.author.id}) tried to claw {user.name}({user.id}) but something went wrong.",
                file=stderr,
            )

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

    @return_member.command(aliases=["basic", "normal", "everyone", "nobody"])
    async def standard(self, ctx, user: discord.Member):
        """Return them as a nobody."""
        if ctx.guild.get_role(483212257237401621) in user.roles:
            await user.remove_roles(
                ctx.guild.get_role(483212257237401621), reason="Returned from Contact claws."
            )
            await ctx.guild.get_channel(350726339327950859).send(
                f"{user.name} has been returned from {ctx.guild.get_channel(483213085293936640).mention}."
            )
