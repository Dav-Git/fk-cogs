from redbot.core import commands
from typing import Optional


def is_dav():
    async def predicate(ctx):
        return ctx.author.id == 428675506947227648

    return commands.check(predicate)


class BadIdea(commands.Cog):
    def __init__(self, bot):
        pass

    @is_dav()
    @commands.command()
    async def test(self, ctx):
        """I use this to test cog code."""
        pass

    @commands.Cog.listener()
    async def on_member_update(self,before,after):
        member= after
        if member.guild.id == 133049272517001216:
            if member.id == 204027971516891136:
                if after.name != before.name:
                    await 
