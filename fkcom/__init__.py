from .fkcom import FKCom


async def setup(bot):
    cog = FKCom(bot)
    await cog.initialize()
    bot.add_cog(cog)
