from redbot.core import checks, commands
import asyncio
import discord


class TruePurge(commands.Cog):
    @checks.admin()
    @commands.command()
    async def truepurge(self, ctx, amount: int):
        async for message in ctx.channel.history(limit=amount):
            for i in range(5):
                i
                await message.delete()
            asyncio.sleep(30)
