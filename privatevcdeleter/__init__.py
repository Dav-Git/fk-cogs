from .privatevcdeleter import PrivateVcDeleter


def setup(bot):
    bot.add_cog(PrivateVcDeleter())