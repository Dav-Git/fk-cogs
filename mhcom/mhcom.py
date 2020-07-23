from redbot.core import commands, checks
import discord


class MHCom(commands.Cog):
    @commands.command()
    @checks.mod()
    async def moderation(self, ctx):
        """Quick reference to moderation commands."""
        text = """```AsciiDoc
[Moderation commands]\n
-check <User>                      | Check flags, warnings and userinfo for a user.
-forcenick <User> [Reason]         | Force-change a user's nickname.
-warn <User> <Reason>              | Warn a user.
-tm <User> [Reason] --for <time>   | -tm <User> [Reason] --for 12 hours | Tempmute a user.    | Alias: -moo
-mute                              | See all muting options including voice or channel mutes.


[Quick-access messages]\n
-admin                             | Get an admin to help you.


[Other]\n
N/A
```"""
        await ctx.send(text)
