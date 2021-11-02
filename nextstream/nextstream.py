from redbot.core import commands
from datetime import datetime, timedelta


class NextStream(commands.Cog):
    """NextStream"""

    def __init__(self):
        pass

    @commands.command()
    async def stream(self, ctx):
        """NextStream"""
        await ctx.send(f"<t:{int(self._next_stream().timestamp())}:d>")

    def _next_stream(self):
        now = datetime.now()
        oneDay = timedelta(days=1)
        while True:
            now += oneDay
            dow = now.strftime("%w")
            if dow == "4":
                return now
