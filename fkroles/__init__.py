from .fkroles import FKRoles

__red_end_user_data_statement__ = "This cog does not store end user data."

async def setup(bot):
    cog = FKRoles(bot)
    await cog.initialize()
    await bot.add_cog(cog)