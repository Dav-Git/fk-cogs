from redbot.core import commands
from datetime import datetime, timedelta


class NextStream(commands.Cog):
    """NextStream"""

    def __init__(self):
        self.skip = 0

    @commands.command()
    async def stream(self, ctx):
        """NextStream"""
        streamTime = int(self._next_stream().timestamp())
        await ctx.send(
            f"The next <:YT_Kitten:545557741947584515> Livestream will be on <t:{streamTime}:F>.\n:alarm_clock: That's in <t:{streamTime}:R>."
        )

    def _next_stream(self):
        now = datetime.now()
        oneDay = timedelta(days=1)
        if self.skip > 0:
            now = now + timedelta(weeks=self.skip)
        while True:
            if now.strftime("%w") == "4":
                now = now.replace(hour=21, minute=0)
                return now
            now += oneDay

    @commands.mod()
    @commands.command()
    async def skipstream(self, ctx, weeks: int = 0):
        """Skip the next x Streams"""
        self.skip = weeks
        await ctx.send(
            f"Skipping the next {weeks} Streams. This needs to be reset in case of a bot restart."
        )
