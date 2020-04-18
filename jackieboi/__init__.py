from .jackieboi import JackieBoi


async def setup(bot):
    cog = JackieBoi(bot)
    await cog.initialize()
    bot.add_cog(cog)
