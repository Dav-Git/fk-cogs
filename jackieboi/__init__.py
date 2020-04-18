from .jackieboi import JackieBoi


def setup(bot):
    cog = Jackieboi(bot)
    await cog.initialize()
    bot.add_cog(cog)
