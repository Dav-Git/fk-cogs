from redbot.core import commands, modlog
import discord
from datetime import datetime
from typing import Union


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
        blocklist_remove_case = {
            "name": "unblocklist",
            "default_setting": True,
            "image": ":white_check_mark:",
            "case_str": "Removed from blocklist",
        }
        try:
            await modlog.register_casetype(**blocklist_add_case)
            await modlog.register_casetype(**blocklist_remove_case)
        except RuntimeError:
            pass

    async def initialize(self, bot):
        await self.register_casetypes()

    @commands.group(aliases=["blacklist", "denylist"])
    @checks.is_owner()
    async def blocklist(self, ctx: commands.Context):
        """
        Blocklist management commands.
        """
        pass

    @blocklist.command(name="add", usage="<user>...")
    async def blocklist_add(self, ctx: commands.Context, *users: Union[discord.Member, int]):
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
                await ctx.send(_("You cannot add an owner to the blocklist!"))
                return

        uids = {getattr(user, "id", user) for user in users}
        await self.bot._whiteblacklist_cache.add_to_blacklist(None, uids)
        for user in users:
            await modlog.create_case(
                ctx.bot, ctx.guild, datetime.now(), "blocklist", user, ctx.author
            )

        await ctx.send(_("User added to blocklist."))

    @blocklist.command(name="list")
    async def blocklist_list(self, ctx: commands.Context):
        """
        Lists users on the blocklist.
        """
        curr_list = await self.bot._whiteblacklist_cache.get_blacklist(None)

        if not curr_list:
            await ctx.send("Blocklist is empty.")
            return

        msg = _("Users on blocklist:")
        for user in curr_list:
            msg += "\n\t- {}".format(user)

        for page in pagify(msg):
            await ctx.send(box(page))

    @blocklist.command(name="remove", usage="<user>...")
    async def blocklist_remove(self, ctx: commands.Context, *users: Union[discord.Member, int]):
        """
        Removes user from the blocklist.
        """
        if not users:
            await ctx.send_help()
            return

        uids = {getattr(user, "id", user) for user in users}
        await self.bot._whiteblacklist_cache.remove_from_blacklist(None, uids)
        for user in users:
            await modlog.create_case(
                ctx.bot, ctx.guild, datetime.now(), "unblocklist", user, ctx.author
            )
        await ctx.send(_("Users have been removed from blocklist."))

    @blocklist.command(name="clear")
    async def blocklist_clear(self, ctx: commands.Context):
        """
        Clears the blocklist.
        """
        await self.bot._whiteblacklist_cache.clear_blacklist()
        await ctx.send(_("Blocklist has been cleared."))