from .customdm import CustomDM


def setup(bot):
    bot.add_cog(CustomDM(bot))
