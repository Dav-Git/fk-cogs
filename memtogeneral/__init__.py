from .memtogeneral import MemToGeneral


def setup(bot):
    bot.add_cog(MemToGeneral(bot))
