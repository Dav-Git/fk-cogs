from typing import Optional, Union
import discord
from discord.ext import tasks
from redbot.core import checks, commands, modlog


class FKBanAppeal(commands.Cog):
    async def red_delete_data_for_user(self, *, requester, user_id):
        pass  # This cog stores no EUD

    def __init__(self, bot):
        self.bot = bot
        self.mod_cog = self.bot.get_cog("Mod")

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(ban_members=True)
    @commands.admin_or_permissions(ban_members=True)
    async def ban(
        self,
        ctx: commands.Context,
        user: Union[discord.Member, commands.RawUserIdConverter],
        days: Optional[int] = 0,
        *,
        reason: str = None,
    ):
        """Ban a user from this server and optionally delete days of messages.

        `days` is the amount of days of messages to cleanup on ban.

        Examples:
           - `[p]ban 428675506947227648 7 Continued to spam after told to stop.`
            This will ban the user with ID 428675506947227648 and it will delete 7 days worth of messages.
           - `[p]ban @Twentysix 7 Continued to spam after told to stop.`
            This will ban Twentysix and it will delete 7 days worth of messages.

        A user ID should be provided if the user is not a member of this server.
        If days is not a number, it's treated as the first word of the reason.
        Minimum 0 days, maximum 7. If not specified, the defaultdays setting will be used instead.
        """
        await ctx.send("Boom boom boom boom, I want you in my room")
        await self.mod_cog.ban_user(user,ctx,days,reason,True)