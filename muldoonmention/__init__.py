from .muldoonmention import MuldoonMention


async def setup(bot):
    await bot.add_cog(MuldoonMention(bot))
