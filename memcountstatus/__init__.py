from .memcountstatus import MemCountStatus

__red_end_user_data_statement__ = "This cog does not store end user data."


async def setup(bot):
    cog = MemCountStatus(bot)
    await bot.add_cog(cog)
