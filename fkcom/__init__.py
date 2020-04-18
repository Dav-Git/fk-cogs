from .fkcom import FKCom


async def setup(bot):
    cog = FKCom()
    await cog.initialize()
    bot.add_cog(cog)
