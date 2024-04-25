from .scraperkiller import ScraperKiller

__red_end_user_data_statement__ = "This cog does not store end user data."


async def setup(bot):
    cog = ScraperKiller(bot)
    await bot.add_cog(cog)
