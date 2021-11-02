from redbot.core import commands
from datetime import datetime
from datetime import timedelta


class NextStream(commands.Cog):
    """NextStream"""

    def __init__(self):
        pass

    @commands.command()
    async def stream(self, ctx):
        """NextStream"""
        await ctx.send(f"<t:{self._next_stream()}:d>")

    def _next_stream(self):
        now = datetime.now()
        while True:
            now += timedelta(days=1)
            dow = now.strftime("%w")
            if dow == 4:
                return now
