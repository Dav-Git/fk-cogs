from .fkbday import FKBday


def setup(bot):
    bot.add_cog(FKBday(bot))
