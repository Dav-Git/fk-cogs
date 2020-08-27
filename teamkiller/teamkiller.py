from redbot.core import commands, Config
from redbot.core.utils.menus import menu, DEFAULT_CONTROLS
from redbot.core.utils.chat_formatting import pagify
from typing import Optional
import discord


class TeamKiller(commands.Cog):
    """Teamkill logging cog."""

    async def red_delete_data_for_user(self, *, requester, user_id):
        async with await self.config.all_members() as data:
            for guild in data:
                for member in data:
                    if member == user_id:
                        del data[guild][member]

    def __init__(self):
        self.config = Config.get_conf(self, 114826082020, force_registration=True)
        self.config.register_member(teamkills=0, teamdeaths=0, hitlist=[], killers=[])

    @commands.group()
    async def teamkill(self, ctx):
        """Teamkill commands"""
        pass

    @teamkill.command()
    async def log(self, ctx, killer: discord.Member, victim: Optional[discord.Member] = None):
        """Log a teamkil"""
        if victim:
            await ctx.send(
                f"{killer.mention} teamkilled {victim.mention}.",
                allowed_mentions=discord.AllowedMentions(users=False),
            )
        else:
            await ctx.send(
                f"{killer.mention} teamkilled someone.",
                allowed_mentions=discord.AllowedMentions(users=False),
            )
        async with self.config.member(killer).all() as data:
            data["teamkills"] += 1
            if victim:
                data["hitlist"].append(victim.id)
        if victim:
            async with self.config.member(victim).all() as data:
                data["teamdeaths"] += 1
                data["killers"].append(killer.id)
        await ctx.tick()

    @teamkill.command()
    async def stats(self, ctx, user: Optional[discord.Member] = None):
        """See your teamkill stats"""
        if user is None:
            user = ctx.author
        data = await self.config.member(user).all()
        embed = discord.Embed(title=f"{user.display_name}'s teamkill stats")
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Teamkills", value=data["teamkills"])
        embed.add_field(name="Teamdeaths", value=data["teamdeaths"])
        killers = "\n".join(ctx.guild.get_member(x).mention for x in data["killers"])
        pages = [embed]
        for page in pagify(killers, page_length=1024):
            em = discord.Embed(
                title=f"{user.display_name} has been teamkilled by", description=page
            )
            em.set_thumbnail(url=user.avatar_url)
            pages.append(em)
        victims = "\n".join(ctx.guild.get_member(x).mention for x in data["hitlist"])
        for page in pagify(victims, page_length=1024):
            em = discord.Embed(title=f"{user.display_name} has teamkilled", description=page)
            em.set_thumbnail(url=user.avatar_url)
            pages.append(em)
        await menu(ctx, pages, DEFAULT_CONTROLS, timeout=120)

    @teamkill.command()
    async def remove(self, ctx, killer: discord.Member, victim: Optional[discord.Member] = None):
        """Remove a teamkill"""
        await ctx.send("Deleting teamkill...")
        async with self.config.member(killer).all() as data:
            if data["teamkills"]:
                data["teamkills"] -= 1
                if victim:
                    data["hitlist"].remove(victim.id)
        if victim:
            async with self.config.member(victim).all() as data:
                data["teamdeaths"] -= 1
                data["killers"].remove(killer.id)
        await ctx.tick()
