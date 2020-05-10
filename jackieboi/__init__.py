from .jackieboi import JackieBoi


async def setup(bot):
    cog = JackieBoi(bot)

    bot.add_cog(cog)
