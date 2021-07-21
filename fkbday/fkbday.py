from redbot.core import commands
import discord
import asyncio


class FKBday(commands.Cog):
    async def isStaff():
        async def predicate(ctx) -> bool:
            staffroles = [
                450253903209168906,
                530016413616963591,
                332835206493110272,
                332834961407213568,
                344440746264231936,
            ]
            userroles = [r.id for r in ctx.author.roles]
            if any(role in userroles for role in staffroles):
                return True
            else:
                return False

        return commands.check(predicate)

    @isStaff()
    @commands.command(aliases=["birthday", "bd"])
    async def bday(self, ctx, *, user: discord.Member):
        """Says happy birthday to a user"""
        await ctx.send("Happy Birthday, **{0}**! :tada:".format(user.display_name))
        await user.add_roles(ctx.guild.get_role(657943577065947157), reason="It's their birthday!")
        await asyncio.sleep(86400)
        try:
            await user.remove_roles(
                ctx.guild.get_role(657943577065947157), reason="Their birthday is over!"
            )
        except:
            await ctx.guild.get_channel(449944250507984896).send(
                "Something went wrong when trying to remove the birthday role from {0}".format(
                    user.display_name
                )
            )
