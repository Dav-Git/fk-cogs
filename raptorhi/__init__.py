from .raptorhi import RaptorHi


async def setup(bot):
    await bot.add_cog(RaptorHi(bot))
