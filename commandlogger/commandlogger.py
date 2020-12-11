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
    @commands.command()
    async def cmdlog(self, ctx, user: discord.Member, *, command: str):
        """Get the command log for a user and command."""
        data = await self.config.member(user).commands()
        pages = []
        for command in data:
            for timestamp in data[command]:
                e = discord.Embed(
                    title=f"Commandlog for {user.mention}", description=f"Command: ``{command}``"
                )
                e.add_field(name="Content", value=data[command][timestamp])
                e.add_field(
                    name="Timestamp",
                    value=datetime.fromtimestamp(float(timestamp)).strftime(
                        "%H:%M:%S | %d %b %Y UTC"
                    ),
                )
                e.color = discord.Color.dark_blue()
                pages.append(e)
        await menu(ctx, e, DEFAULT_CONTROLS, timeout=120)
