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

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        role_ids = await self.config.all_roles()
        after_role_ids = [role.id for role in after.roles]
        for role_id in role_ids:
            if role_id in after_role_ids:
                excluded = False
                for rid in role_ids[role_id]["exclude_roles"]:
                    if rid in after_role_ids:
                        excluded = True
                if excluded:
                    continue
                else:
                    await after.remove_roles(after.guild.get_role(role_id))
                    await after.add_roles(
                        *[after.guild.get_role(r_id) for r_id in role_ids[role_id]["assign_roles"]]
                    )
            else:
                continue

    @commands.admin()
    @commands.group()
    async def rpc(self, ctx):
        """RolePromotionChecker commands"""
        pass

    @rpc.command()
    async def addrole(self, ctx, scan_role: discord.Role, *assign_roles: discord.Role):
        """Add a role to the list of roles that are scanned regularly and define which role should be assigned when the scanrole is found on a user."""
        await self.config.role(scan_role).assign_roles.set([r.id for r in assign_roles])
        await ctx.send(
            f"Added {scan_role.name} to the list of roles that are scanned regularly.\nThe roles {[r.mention for r in assign_roles]} will be assigned."
        )

    @rpc.command()
    async def setexclusions(self, ctx, scan_role: discord.Role, *exclude_roles: discord.Role):
        """Add a role to the list of roles that exclude a user from the scan.
        Leave Empty, to remove all exclusions from the scanrole."""
        await self.config.role(scan_role).exclude_roles.set([r.id for r in exclude_roles])
        await ctx.send(
            f"Members with the roles {[r.mention for r in exclude_roles]} will be excluded when scanning {scan_role.mention}"
        )