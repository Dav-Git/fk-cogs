from redbot.core import commands, Config
from redbot.core.utils.menus import menu, DEFAULT_CONTROLS
import discord
from datetime import datetime


class CommandLogger(commands.Cog):
    def __init__(self):
        self.config = Config.get_conf(self, 123456, True)
        self.config.register_member(commands={})
        # Data structure: commands = {"name":{timestamp:"content"}}

    @commands.Cog.listener()
    async def on_command(self, ctx: commands.Context):
        async with self.config.member(ctx.author).commands() as commands_dict:
            try:
                commands_dict[ctx.command.qualified_name][
                    datetime.now().timestamp()
                ] = ctx.message.content
            except KeyError:
                name_dict = {datetime.now().timestamp(): ctx.message.content}
                commands_dict[ctx.command.qualified_name] = name_dict

    @commands.is_owner()
    @commands.group()
    async def cmdlog(self, ctx):
        """Commandlog"""
        pass

    @cmdlog.command(name="user")
    async def cmdlog_user(self, ctx, user: discord.Member):
        """Get the command log for a user."""
        data = await self.config.member(user).commands()
        pages = []
        for command in data:
            for timestamp in data[command]:
                e = discord.Embed(
                    title=f"Commandlog for {user.display_name}",
                    description=f"Command: ``{command}``",
                )
                e.add_field(name="Content", value=data[command][timestamp], inline=False)
                e.add_field(
                    name="Timestamp",
                    value=self._timestamp_to_string(timestamp),
                )
                e.color = discord.Color.dark_blue()
                e.set_thumbnail(url=ctx.guild.get_member(user).avatar_url)
                pages.append(e)
        pages.reverse()
        await menu(ctx, pages, DEFAULT_CONTROLS, timeout=120)

    @cmdlog.command(name="both")
    async def cmdlog_command_and_user(self, ctx, user: discord.Member, *, command: str):
        """Get the command log for a user using a specified command."""
        data = await self.config.member(user).commands()
        pages = []
        for timestamp in data[command]:
            e = discord.Embed(
                title=f"Commandlog for {user.display_name}",
                description=f"Command: ``{command}``",
            )
            e.add_field(name="Content", value=data[command][timestamp], inline=False)
            e.add_field(
                name="Timestamp",
                value=self._timestamp_to_string(timestamp),
            )
            e.color = discord.Color.green()
            e.set_thumbnail(url=ctx.guild.get_member(user).avatar_url)
            pages.append(e)
        pages.reverse()
        await menu(ctx, pages, DEFAULT_CONTROLS, timeout=120)

    @cmdlog.command(name="command")
    async def cmdlog_command(self, ctx, *, command: str):
        """Get the command log for a user using a specified command."""
        members = await self.config.all_members(ctx.guild)
        pages = []
        for member in members:
            data = members[member]["commands"]
            try:
                for timestamp in data[command]:
                    user = ctx.guild.get_member(member)
                    e = discord.Embed(
                        title=f"Commandlog for ``{command}``",
                        description=f"Invoked by: {user.mention}({user.name}#{user.discriminator} {user.id}",
                    )
                    e.add_field(name="Content", value=data[command][timestamp], inline=False)
                    e.add_field(
                        name="Timestamp",
                        value=self._timestamp_to_string(timestamp),
                    )
                    e.color = discord.Color.dark_orange()
                    e.set_thumbnail(url=ctx.guild.get_member(member).avatar_url)
                    pages.append(e)
            except KeyError:
                pass
        pages.reverse()
        try:
            await menu(ctx, pages, DEFAULT_CONTROLS, timeout=120)
        except IndexError:
            await ctx.send("Command not tracked yet.")

    @commands.is_owner()
    @commands.command(name="raw")
    async def commandlog_raw(self, ctx, command: str, *, arguments: str):
        """Get the uses of an exact command"""
        members = await self.config.all_members(ctx.guild)
        pages = []
        for member in members:
            data = members[member]["commands"]
            try:
                for timestamp in data[command]:
                    if data[command][timestamp] == f"-{command} {arguments}":
                        user = ctx.guild.get_member(member)
                        e = discord.Embed(
                            title=f"Commandlog for ``-{command} {arguments}``",
                            description=f"Invoked by: {user.mention}({user.name}#{user.discriminator} {user.id}",
                        )
                        e.add_field(
                            name="Timestamp",
                            value=self._timestamp_to_string(timestamp),
                        )
                        e.color = discord.Color.dark_orange()
                        e.set_thumbnail(url=user.avatar_url)
                        pages.append(e)
            except KeyError:
                pass
        pages.reverse()
        try:
            await menu(ctx, pages, DEFAULT_CONTROLS, timeout=120)
        except IndexError:
            await ctx.send("Command not tracked yet.")

    def _timestamp_to_string(self, timestamp):
        return datetime.fromtimestamp(float(timestamp)).strftime("%H:%M:%S | %d %b %Y EST")