from .sentry import Sentry


def setup(bot):
    bot.add_cog(Sentry())