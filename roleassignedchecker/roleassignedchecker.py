import discord
from discord.ext import tasks
from redbot.core import commands, Config


class RoleAssignedChecker(commands.Cog):
    """RoleAssignedChecker"""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=171120211734)
        default_guild = {"assign_role": None, "exclude_roles": []}
        self.config.register_guild(**default_guild)
        self.check_task.start()

    def cog_unload(self):
        """Things that happen on cog unload"""
        self.check_task.cancel()

    async def initialize(self):
        """Initialize the cog"""
        self.check_task()

    @tasks.loop(minutes=1)
    async def check_task(self):  # pylance: disable=unused-argument
        guilds_data = await self.config.all_guilds()
        for guild_id in guilds_data:
            guild = self.bot.get_guild(guild_id)
            if guild is None:
                continue
            guild_data = guilds_data[guild_id]
            role = guild.get_role(guild_data["assign_role"])
            if role is None:
                continue
            for member in guild.members:
                if len(member.roles) == 1:
                    await member.add_roles(role)
            ##    if not role in member.roles:
            ##        if any(
            ##            exclude_role in guild_data["exclude_roles"]
            ##            for exclude_role in [r.id for r in member.roles]
            ##        ):
            ##            continue

    @commands.admin()
    @commands.group()
    async def rac(self, ctx):
        """RoleAssignedChecker commands"""
        pass

    @rac.command()
    async def setrole(self, ctx, role: discord.Role):
        """Set the role to check for and assign"""
        await self.config.guild(ctx.guild).assign_role.set(role.id)
        await ctx.send(f"Role {role.mention} will be checked and assigned")

    @rac.command()
    async def setexclusions(self, ctx, *exclude_roles: discord.Role):
        """Add a role to the list of roles that exclude a user from the scan.
        Leave Empty, to remove all exclusions."""
        await self.config.guild(ctx.guild).exclude_roles.set([r.id for r in exclude_roles])
        await ctx.send(
            f"Members with the roles {[r.mention for r in exclude_roles]} will be excluded when scanning."
        )

    @rac.command()
    async def show(self, ctx):
        """Show the current RoleAssignedChecker setup"""
        data = await self.config.guild(ctx.guild).all()
        await ctx.send(
            f"RoleAssignedChecker is set to check for role {ctx.guild.get_role(data['assign_role']).mention} and assign it if it is not found."
        )
        await ctx.send(
            f"Members with the roles {[ctx.guild.get_role(r).mention for r in data['exclude_roles']]} will be excluded when scanning."
        )
