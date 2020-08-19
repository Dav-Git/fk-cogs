from redbot.core import commands
import subprocess
import os
from typing import Optional


def is_dav():
    async def predicate(ctx):
        return ctx.author.id == 428675506947227648

    return commands.check(predicate)


class BadIdea(commands.Cog):
    def __init__(self, bot):
        self.warnsystem = bot.get_cog("WarnSystem").api

    @is_dav()
    @commands.command()
    async def test(self, ctx):
        await self.warnsystem.warn(ctx.guild, ctx.author, ctx.author, 1, "test reason")

