from redbot.core import commands


class FkPingSafe(commands.Cog):
    @commands.mod()
    @commands.command(aliases=["ps", "noping"])
    async def pingsafe(self, ctx):
        """Get or remove the staff pingsafe role"""
        PINGSAFE_ROLE = ctx.guild.get_role(775359048342044713)
        if PINGSAFE_ROLE in ctx.author.roles:
            await ctx.author.remove_roles(PINGSAFE_ROLE)
            await ctx.tick()
            await ctx.send(f"{ctx.author.display_name} you had the Ping Safe role removed.")
        else:
            await ctx.author.add_roles(PINGSAFE_ROLE)
            await ctx.tick()
            await ctx.send(f"{ctx.author.display_name} you had the Ping Safe role added.")