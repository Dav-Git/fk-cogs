from .dungeonkick import DungeonKick


def setup(bot):
    bot.add_cog(DungeonKick(bot))
