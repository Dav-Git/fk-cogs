from .thedot import TheDot

__red_end_user_data_statement__ = "This cog does not store end user data."


async def setup(bot):
    await bot.add_cog(TheDot())
