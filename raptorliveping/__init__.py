from .raptorliveping import RaptorLivePing


async def setup(bot):
    await bot.add_cog(RaptorLivePing())
