from .claw import Claw

__end_user_data_statement__ = "This cog does not store end user data."


async def setup(bot):
    cog = Claw()
    await cog.initialize()
    bot.add_cog(cog)
