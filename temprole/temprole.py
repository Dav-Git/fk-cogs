from datetime import datetime, timedelta
from typing import Optional

import logging
import discord
from discord.ext import tasks
from redbot.core import Config, checks, commands, modlog
from redbot.core.utils.menus import DEFAULT_CONTROLS, menu


class TempRole(commands.Cog):
    async def red_delete_data_for_user(self, *, requester, user_id):
        if requester == "owner" or requester == "discord_deleted_user":
            await self._update_cache()
            self.log.info(f"Starting deletion for {user_id}")
            for guild_id in self.cache:
                for member_id in self.cache[guild_id]:
                    if int(member_id) == user_id:
                        if self.cache[guild_id][member_id]["temproles"]:
                            mem_roles = self.cache[guild_id][member_id]["temproles"]
                            guild = self.bot.get_guild(int(guild_id))
                            member = guild.get_member(int(member_id))
                            for role_id in mem_roles:
                                role = guild.get_role(int(role_id))
                                try:
                                    await member.remove_roles(
                                        role, reason="Data deletion request."
                                    )
                                except discord.errors.Forbidden:
                                    self.log.warning(
                                        f"Couldn't remove role {role_id} from {member_id} in {guild_id} due to insufficient permissions."
                                    )
                                async with self.config.member(member).temproles() as temproles:
                                    try:
                                        del temproles[role.id]
                                    except KeyError:
                                        pass
                                await self._update_cache()
            self.log.info("Data deletion complete.")

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, 101, force_registration=True)
        default_member = {"temproles": {}}
        self.config.register_member(**default_member)
        self.log = logging.getLogger("red.cog.dav-cogs.temprole")
        self.task.start()
        self.cache = None

    def cog_unload(self):
        self.task.cancel()

    @tasks.loop(minutes=5)
    async def task(self):
        self.log.info("Running temprole task")
        if self.cache is None:
            await self._update_cache()
        for guild_id in self.cache:
            for member_id in self.cache[guild_id]:
                if self.cache[guild_id][member_id]["temproles"]:
                    mem_roles = self.cache[guild_id][member_id]["temproles"]
                    guild = self.bot.get_guild(int(guild_id))
                    member = guild.get_member(int(member_id))
                    for role_id in mem_roles:
                        if (
                            datetime.fromtimestamp(
                                self.cache[guild_id][member_id]["temproles"][role_id]
                            )
                            < datetime.now()
                        ):
                            role = guild.get_role(int(role_id))
                            try:
                                await member.remove_roles(role, reason="Temprole expired.")
                            except discord.errors.Forbidden:
                                self.log.warning(
                                    f"Couldn't remove role {role_id} from {member_id} in {guild_id} due to insufficient permissions."
                                )
                            async with self.config.member(member).temproles() as temproles:
                                try:
                                    del temproles[role.id]
                                except KeyError:
                                    pass
                            await self._update_cache()

    async def initialize(self):
        await self.register_casetypes()

    async def _update_cache(self):
        self.cache = await self.config.all_members()

    @staticmethod
    async def register_casetypes():
        temprole_case = {
            "name": "temprole",
            "default_setting": True,
            "image": "\N{CLOCK FACE TEN OCLOCK}\N{VARIATION SELECTOR-16}",
            "case_str": "Temporary role applied",
        }
        try:
            await modlog.register_casetype(**temprole_case)
        except RuntimeError:
            pass

    @checks.mod()
    @commands.group()
    async def temprole(self, ctx):
        pass

    @temprole.command()
    async def add(
        self,
        ctx,
        role: discord.Role,
        member: discord.Member,
        duration: commands.TimedeltaConverter,
        reason: Optional[str],
    ):
        try:
            await member.add_roles(role, reason=reason)
        except discord.errors.Forbidden:
            await ctx.send("Insufficient Permissions")
            return
        expiry = datetime.now() + duration
        async with self.config.member(member).temproles() as temproles:
            temproles[role.id] = expiry.timestamp()
        await modlog.create_case(
            self.bot,
            ctx.guild,
            datetime.now(),
            "temprole",
            member,
            moderator=ctx.author,
            reason=reason,
            until=expiry,
            channel=ctx.channel,
        )
        await self._update_cache
        await ctx.tick()

    @temprole.command()
    async def remove(self, ctx, role: discord.Role, member: discord.Member, reason: Optional[str]):
        await member.remove_roles(role, reason=reason)
        async with self.config.member(member).temproles() as temproles:
            try:
                del temproles[role.id]
            except KeyError:
                await ctx.send(
                    f"This user did not have the role {role.name} as temprole.", delete_after=15
                )
        await self._update_cache()
        await ctx.tick()

    @temprole.command(name="list")
    async def list_temproles(self, ctx):
        rendered = []
        await ctx.send("This may take a while...")
        data = await self.config.all_members(guild=ctx.guild)
        for member_id in data:
            if data[member_id]["temproles"]:
                mem_roles = data[member_id]["temproles"]
                member = ctx.guild.get_member(member_id)
                em = discord.Embed(title=member.display_name, color=await ctx.embed_color())
                em.set_thumbnail(url=member.avatar_url)
                for role_id in mem_roles:
                    role = ctx.guild.get_role(int(role_id))
                    em.add_field(
                        name=role.name,
                        value=f"Expires {datetime.fromtimestamp(mem_roles[role_id]).strftime('%d %B %Y | %H:%M')}",
                        inline=False,
                    )
                rendered.append(em)
        if rendered:
            await menu(ctx, rendered, DEFAULT_CONTROLS)
        else:
            await ctx.send("No members are currently in a temprole.", delete_after=15)
