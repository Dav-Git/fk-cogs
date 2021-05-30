from .sentry import Sentry


def setup(bot):
    cog = Sentry(bot)
    bot.add_cog(cog)
    cog.initialize()