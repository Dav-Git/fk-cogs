from .dacow import DaCow

__end_user_data_statement__ = "This cog does not store end user data."


def setup(bot):
    bot.add_cog(DaCow())
