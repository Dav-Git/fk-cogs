from .customdm import CustomDM

__red_end_user_data_statement__ = "This cog does not store end user data."


def setup(bot):
    bot.add_cog(CustomDM(bot))
