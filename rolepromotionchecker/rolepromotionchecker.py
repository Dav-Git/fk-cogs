from typing import List
import discord
from redbot.core import commands, Config


class RolePromotionChecker(commands.Cog):
    """RolePromotionChecker"""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=171120211734)
        default_role = {"assign_roles": [], "exclude_roles": []}
        self.config.register_role(**default_role)

    @commands.admin()
    @commands.group()
    async def rpc(self, ctx):
        """RolePromotionChecker commands"""
        pass

    @rpc.command()
    async def addrole(self, ctx, scan_role: discord.Role, *, assign_roles: List[discord.Role]):
        """Add a role to the list of roles that are scanned regularly and define which role should be assigned when the scanrole is found on a user."""
        await self.config.role(scan_role).assign_roles.set(assign_roles)
        await ctx.send(
            f"Added {scan_role.name} to the list of roles that are scanned regularly.\nThe roles {[r.mention for r in assign_roles]} will be assigned."
        )

    @rpc.command()
    async def setexclusions(
        self, ctx, scan_role: discord.Role, *, exclude_roles: List[discord.Role]
    ):
        """Add a role to the list of roles that exclude a user from the scan.
        Leave Empty, to remove all exclusions from the scanrole."""
        await self.config.role(scan_role).exclude_roles.set(exclude_roles)
        await ctx.send(
            f"Members with the roles {[r.mention for r in exclude_roles]} will be excluded when scanning {scan_role.mention}"
        )
