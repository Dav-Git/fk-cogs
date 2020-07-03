from redbot.core import checks, commands
import asyncio
import discord


class TruePurge(commands.Cog):
    @checks.admin()
    @commands.command()
    async def truepurge(self, ctx, amount: int):
        """Purge a channel.\n\nSet the amount to -1 to clear all of it."""
        if amount == -1:
            amount = None
        await ctx.send("Starting...")
        async for message in ctx.channel.history(limit=amount):
            try:
                await message.delete()
            except discord.errors.NotFound:
                pass
            await asyncio.sleep(0.2)
        await ctx.send("Done", delete_after=30)
