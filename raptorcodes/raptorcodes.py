from typing import List

import discord
from redbot.core import Config, commands
from redbot.core.utils.chat_formatting import pagify


class RaptorCodes(commands.Cog):

    def __init__(self, bot):
        self.config = Config.get_conf(self, identifier=201120252116)
        default_global = {"codes": []}
        self.config.register_global(**default_global)

    async def red_delete_data_for_user(self, *, requester, user_id):
        pass

    @commands.group()
    @commands.mod()
    async def codes(self, ctx):
        """Manage giveaway codes"""
        pass

    @codes.command()
    async def show(self, ctx):
        """Show all giveaway codes"""
        codes = await self.config.codes()
        if not codes:
            await ctx.send("No giveaway codes available.")
            return
        message: str = "# Current giveaway codes:\n" + "\n".join(codes)
        for page in pagify(message):
            await ctx.send(page)

    @codes.group()
    async def add(self, ctx):
        """Add giveaway codes"""
        pass

    @add.command()
    async def top(self, ctx, codes: str):
        """Add codes to the top of the list"""
        codes = codes.split(",")
        current_codes = await self.config.codes()
        new_codes = codes + current_codes
        await self.config.codes.set(new_codes)
        await ctx.send(f"Added {len(codes)} codes to the top of the list.")

    @add.command()
    async def bottom(self, ctx, codes: str):
        """Add codes to the bottom of the list"""
        codes = codes.split(",")
        current_codes = await self.config.codes()
        new_codes = current_codes + codes
        await self.config.codes.set(new_codes)
        await ctx.send(f"Added {len(codes)} codes to the bottom of the list.")

    @codes.command()
    async def clear(self, ctx):
        """Clear all giveaway codes"""
        await self.config.codes.set([])
        await ctx.send("All giveaway codes have been cleared.")

    @codes.command()
    async def remove(self, ctx, code: str):
        """Remove a specific giveaway code"""
        current_codes = await self.config.codes()
        if code in current_codes:
            current_codes.remove(code)
            await self.config.codes.set(current_codes)
            await ctx.send(f"Removed code: {code}")
        else:
            await ctx.send(f"Code not found: {code}")

    @codes.command()
    async def send(self, ctx, amount: int, member: discord.Member):
        """Send a number of giveaway codes to a member via DM"""
        current_codes = await self.config.codes()
        if amount > len(current_codes):
            await ctx.send(f"Not enough codes available. Only {len(current_codes)} codes left.")
            return
        codes_to_send = current_codes[:amount]
        remaining_codes = current_codes[amount:]
        await self.config.codes.set(remaining_codes)

        try:
            await member.send(
                "Here is your prize from the SeaRaptor giveaway:\n" + "\n".join(codes_to_send)
            )
            await ctx.send(f"Sent {amount} codes to {member.mention}.")
        except discord.Forbidden:
            await ctx.send(f"Could not send DM to {member.mention}.")
