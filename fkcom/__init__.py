from .fkcom import FKCom

__red_end_user_data_statement__ = "This cog does not store end user data."


async def setup(bot):
    cog = FKCom()
    await cog.initialize()
    bot.add_cog(cog)
