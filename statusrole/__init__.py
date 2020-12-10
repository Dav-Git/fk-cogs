from .statusrole import Statusrole


async def setup(bot):
    cog = Statusrole(bot)
    bot.add_cog(cog)