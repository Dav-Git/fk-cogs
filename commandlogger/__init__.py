from .commandlogger import CommandLogger

__red_end_user_data_statement__ = (
    "This cog stores user IDs and command execution metadata for logging purposes."
)


async def setup(bot):
    await bot.add_cog(CommandLogger())
