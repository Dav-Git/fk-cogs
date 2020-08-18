from .botcredits import BotCredits

__red_end_user_data_statement__ = "This cog stores no end user data."


def setup(bot):
    bot.add_cog(BotCredits(bot))
