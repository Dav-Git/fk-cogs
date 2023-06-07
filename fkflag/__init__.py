from .flag import Flag

__red_end_user_data_statement__ = "This cog stores user IDs and notes attached to those user IDs by moderators.\nYou may only request deletion of this data on legal grounds or through a discord data deletion request.\nOperational data (such as logs) will be retained unless otherwise legally required."


async def setup(bot):
    await bot.add_cog(Flag(bot))
