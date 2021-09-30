from .joinflag import JoinFlag

__red_end_user_data_statement__ = "This cog does stores moderation notes attached to a user ID. The notes will be displayed when a user joins the server."


def setup(bot):
    bot.add_cog(JoinFlag())