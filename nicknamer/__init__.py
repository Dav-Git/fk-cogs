from .nicknamer import NickNamer


async def setup(bot):
    cog = NickNamer()
    bot.add_cog(cog)
