from redbot.core import commands, checks
import discord
from typing import Optional


class AshleyCom(commands.Cog):
    async def red_delete_data_for_user(self, *, requester, user_id):
        return

    @commands.command()
    async def mh(self, ctx, user: Optional[discord.Member]):
        """Mental health advisory"""
        await ctx.send(
            "{}{}Feeling like you or someone you know needs help or a place to vent some negative feelings and don't know where to start?  Please visit The Mental Health Together Discord.  They have resources help you and can give advice or guide you in the right direction. The server has areas to vent, share your story and get in touch with others.  There are also some fun areas to share hobbies like food, cute animal pics, etc.\n\nPlease feel free to visit or invite your friends with this link: <https://discord.mhtogether.com/>".format(
                user.mention if user != None else "\u200b", " " if user != None else "\u200b"
            )
        )

    @commands.command(name="mod")
    async def get_mod_attention(self, ctx):
        """Get a moderator to help you."""
        modrolestr = ctx.guild.get_role(432569840524591104).mention
        await ctx.send("A {} has been requested.".format(modrolestr))
        await ctx.guild.get_channel(622996958826463262).send(
            "A {} has been requested in {}.".format(modrolestr, ctx.channel.mention),
            allowed_mentions=discord.AllowedMentions(roles=True),
        )

    @commands.command()
    @checks.mod()
    async def moderation(self, ctx):
        """Quick reference to moderation commands."""
        text = """```AsciiDoc
[Moderation commands]\n
-forcenick <User> [Reason]             | Force-change a user's nickname.
-flag <User> <Reason>                  | Flag a user (staff notes).
-warn <User> <Reason>                  | Warn a user.
-mute <User> [duration] [Reason]       | Mute a user. Provide a duration to make it a tempmute. 
-channelmute <User> [duration] [Reason]| Mute a user in a channel.
-voicemute <User> [Reason]             | Mute a user in a voicechannel.
-voiceban                              | Ban a user from all voicechannels.
-activemutes                           | See all curently active mutes.


[Quick-access messages]\n
N/A


[Other]\n
-bug <Title> [Priority 1-3] <Text>         | Something is broken? Report it here. Staff only.
-enhancement <Title> [Priority 1-3] <Text> | You have an idea on how to do something better? Put it here. Staff only.
-feature <Title> [Priority 1-3] <Text>     | You have a new feature idea? This is your command. Staff only.
 ! IMPORTANT: If your title consists of more than one word make sure to wrap it in quotes. "This title"
              The default priority is 1/low.
```"""
        await ctx.send(text)