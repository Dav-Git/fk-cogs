from .memcountstatus import MemCountStatus


def setup(bot):
    cog = MemCountStatus(bot)
    bot.add_cog(cog)
