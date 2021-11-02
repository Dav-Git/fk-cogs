from redbot.core import commands
from datetime import datetime, timedelta


class NextStream(commands.Cog):
    """NextStream"""

    def __init__(self):
        pass

    @commands.command()
    async def stream(self, ctx):
        """NextStream"""
        streamTime = int(self._next_stream().timestamp())
        await ctx.send(
            f"The next :YT_Kitten: Livestream will be on <t:{streamTime}:F>.\n:alarm_clock: That's in <t:{streamTime}:R>."
        )

    def _next_stream(self):
        now = datetime.now()
        oneDay = timedelta(days=1)
        while True:
            now += oneDay
            dow = now.strftime("%w")
            if dow == "4":
                now = now.replace(hour=21, minute=0)
                return now
