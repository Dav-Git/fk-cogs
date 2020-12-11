from redbot.core import commands, modlog
import discord
from datetime import datetime


class CustomBlockList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    async def register_casetypes():
        blocklist_add_case = {
            "name": "blocklist",
            "default_setting": True,
            "image": ":no_pedestrians:",
            "case_str": "Added to blocklist",
        }
        try:
            await modlog.register_casetype(**blocklist_add_case)
        except RuntimeError:
            pass

    async def initialize(self):
        await self.register_casetypes()

        command_group = bot.get_command("blocklist").add_command(bot.get_command("blocklist_add"))

    @commands.command(usage="<user>...")
    async def blocklist_add(self, ctx: commands.Context, *users: discord.Member):
        """
        Adds a user to the blocklist.
        """
        if not users:
            await ctx.send_help()
            return

        for user in users:
            if isinstance(user, int):
                user_obj = discord.Object(id=user)
            else:
                user_obj = user
            if await ctx.bot.is_owner(user_obj):
                await ctx.send(("You cannot add an owner to the blocklist!"))
                return

        uids = {getattr(user, "id", user) for user in users}
        await self.bot._whiteblacklist_cache.add_to_blacklist(None, uids)
        for user in users:
            await modlog.create_case(
                self.bot, ctx.guild, datetime.now(), "blocklist", user, ctx.author
            )

        await ctx.send(("User added to blocklist."))