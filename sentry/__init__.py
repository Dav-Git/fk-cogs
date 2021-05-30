from .sentry import Sentry


async def setup(bot):
    cog = Sentry(bot)
    bot.add_cog(cog)
    await cog.initialize()