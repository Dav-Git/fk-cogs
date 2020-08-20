from .racemock import RaceMock

__red_end_user_data_statement__ = "No end user data is stored."


def setup(bot):
    bot.add_cog(RaceMock())
