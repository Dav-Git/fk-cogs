from .truepurge import TruePurge


async def setup(bot):
    await bot.add_cog(TruePurge())
