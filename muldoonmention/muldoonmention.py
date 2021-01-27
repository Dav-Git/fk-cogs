from redbot.core import commands
from random import choice


class MuldoonMention(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_without_command(self, message):
        if message.author.bot:
            return
        mentioned_ids = [m.id for m in message.mentions]
        if self.bot.user.id in mentioned_ids:
            quotes = [
                "They should all be destroyed.",
                "Clever girl.",
                "They show extreme intelligence, even problem-solving intelligence.",
                "That one... when she looks at you, you can see she's working things out.",
                "Damn it, even Nedry knew better than to mess with the raptor fences.",
                "Shoot her!",
                "Quiet, all of you!",
                "I want tasers on full charge.",
                "The raptor fences aren't out, are they?",
                "We're being hunted. From the bushes straight ahead.",
                "You ready to live dangerously?",
                "Believe me, all the problems we have so far are nothing compared with what we'd have if the raptors ever got out of their holding pen.",
                "Raptors are smart. Very smart.",
                "Fine dining tonight.",
                "I'm not going in there until daylight.",
                "Not a nice way to go.  Maybe there's justice in the world after all.",
                "Bloody fools.  They're still talking about tourists.",
                "That's not really the question, Mr. Hammond.  The question is, what are they going to do to us?",
                "The electrified fences were off?  All of them?  Since five this morning?",
                "The thing about these damn dinos is that... they don't die fast, even with a direct hit to the brain. ",
                "About all we can hope to do is blow them apart.",
                "This isn't looking good.",
            ]
            await message.channel.send(choice(quotes))
