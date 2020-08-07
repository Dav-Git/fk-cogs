from redbot.core import commands
import subprocess
import os
from typing import Optional


def is_dav():
    async def predicate(ctx):
        return ctx.author.id == 428675506947227648

    return commands.check(predicate)


class BadIdea(commands.Cog):
    async def _bots(self):
        subprocess.run("sudo systemctl restart fkred")
        subprocess.run("sudo systemctl restart aurora")
        subprocess.run("sudo systemctl restart ashley")
        subprocess.run("sudo systemctl restart testo")

    @commands.group()
    @is_dav()
    async def sr(self, ctx):
        """System restart commands. Dav only."""
        pass

    @sr.command(aliases=["lavalink"])
    async def ll(self, ctx, restart_bots: Optional[bool] = True):
        subprocess.run("sudo systemctl restart lavalink")
        if restart_bots:
            await self._bots()
        await ctx.tick()

    @sr.command(aliases=["dashboard"])
    async def dash(self, ctx):
        subprocess.run("sudo systemctl restart fkreddash")
        subprocess.run("sudo systemctl restart auroradash")
        subprocess.run("sudo systemctl restart ashleydash")
        subprocess.run("sudo systemctl restart testodash")
        await ctx.tick()

    @sr.command()
    async def bot(self, ctx, botname: str):
        if botname in ["fkred", "ashley", "aurora", "testo", "all"]:
            if botname == "all":
                await self._bots()
            else:
                os.system(f"sudo /usr/bin/systemctl restart {botname}")
