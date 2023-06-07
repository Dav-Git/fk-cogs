from redbot.core import commands, Config
from typing import Optional


def is_dav():
    async def predicate(ctx):
        return ctx.author.id == 428675506947227648

    return commands.check(predicate)


class BadIdea(commands.Cog):
    def __init__(self, bot):
        self.config = Config.get_conf(self, identifier=123, force_registration=True)
        self.config.register_guild(lastslime=None)

    @is_dav()
    @commands.command()
    async def test(self, ctx):
        """I use this to test cog code."""
        pass
