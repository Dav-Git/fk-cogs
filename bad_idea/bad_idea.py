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

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        member = after
        if member.guild.id == 133049272517001216:
            if member.id == 204027971516891136:
                if after.name != await self.config.guild(after.guild).lastslime():
                    await after.guild.get_channel(171665724262055936).send(
                        f"Slime changed his name from {await self.config.guild(after.guild).lastslime()} to {after.name}\n{after.guild.get_member(428675506947227648).mention}"
                    )
                    await self.config.guild(after.guild).lastslime.set(after.name)
                elif after.nick != before.nick:
                    await after.guild.get_channel(171665724262055936).send(
                        f"Slime changed his nick from {before.nick} to {after.nick}\n{after.guild.get_member(428675506947227648).mention}"
                    )
