from redbot.core import checks, commands
import asyncio
import discord


class TruePurge(commands.Cog):
    @checks.admin()
    @commands.command()
    async def truepurge(self, ctx, amount: int):
        await ctx.send("Starting...", delete_after=30)
        async for message in ctx.channel.history(limit=amount):
            for i in range(5):
                try:
                    await message.delete()
                except discord.errors.NotFound:
                    pass
            asyncio.sleep(30)
        await ctx.send("Done", delete_after=30)
