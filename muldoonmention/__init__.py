from .muldoonmention import MuldoonMention


def setup(bot):
    bot.add_cog(MuldoonMention(bot))
