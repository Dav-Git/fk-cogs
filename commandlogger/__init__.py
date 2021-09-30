from .commandlogger import CommandLogger

__red_end_user_data_statement__ = (
    "This cog stores user IDs and command execution metadata for logging purposes."
)


def setup(bot):
    bot.add_cog(CommandLogger())