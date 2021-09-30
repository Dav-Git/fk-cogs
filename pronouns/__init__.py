from .pronouns import Pronouns

__red_end_user_data_statement__ = "This cog does not store end user data. All data is stored within discord itself and can be removed by clearing your pronouns or talking to a member of staff."


def setup(bot):
    bot.add_cog(Pronouns(bot))