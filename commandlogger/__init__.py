from .commandlogger import CommandLogger


def setup(bot):
    bot.add_cog(CommandLogger())