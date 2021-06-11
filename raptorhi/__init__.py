from .raptorhi import RaptorHi


def setup(bot):
    bot.add_cog(RaptorHi(bot))