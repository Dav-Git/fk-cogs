from .fkcom import FKCom

__red_end_user_data_statement__ = "This cog does not store end user data."


async def setup(bot):
    cog = FKCom(bot)
    bot.add_cog(cog)
    await cog.initialize()
