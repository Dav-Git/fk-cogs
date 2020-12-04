from .statusrole import Statusrole


async def setup(bot):
    cog = Statusrole()
    bot.add_cog(cog)
    await cog.initialize(bot)