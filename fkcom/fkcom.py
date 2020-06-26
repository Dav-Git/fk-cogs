from typing import Optional
import discord
from redbot.core import checks, commands


class FKCom(commands.Cog):
    @commands.command()
    async def bot(self, ctx):
        """If someone requests a bot is put in... run this."""
        await ctx.send(
            f"""In an effort to keep confusion and management requirements at a minimum we have opted to be a one-bot-server.
This means that we will not be adding any other bot besides {ctx.bot.user.mention}.
If you would like to request some sort of functionality please describe exactly what you want to see in {ctx.guild.get_channel(340124332111953942).mention} and we will check if it is something we can implement."""
        )

    @commands.command()
    async def rp(self, ctx, user: Optional[discord.User]):
        """Blanket warn message for rp questions"""
        await ctx.send(
            "Hey{}, it seems like you have asked a question about ARP (Aspirant Gaming). We are not affiliated with ARP at all and sadly can not provide any information to you. To receive an answer to your question, try {} or the Aspirant Gaming discord server.".format(
                " " + user.mention if user != None else "\u200b",
                ctx.guild.get_channel(478917077705555970).mention,
            )
        )

    @commands.command(name="mod")
    async def get_mod_attention(self, ctx):
        """Get a moderator to help you."""
        modrolestr = ctx.guild.get_role(332835206493110272).mention
        await ctx.send("A {} has been requested.".format(modrolestr))
        await ctx.guild.get_channel(339741123406725121).send(
            "A {} has been requested in {}.".format(modrolestr, ctx.channel.mention)
        )

    @commands.command(name="admin")
    async def get_admin_attention(self, ctx):
        """Get an admin to help you."""
        adminrolestr = ctx.guild.get_role(332834961407213568).mention
        await ctx.send("An {} has been requested.".format(adminrolestr))
        await ctx.guild.get_channel(360478963115491328).send(
            "An {} has been requested in {}.".format(adminrolestr, ctx.channel.mention)
        )

    @commands.command(name="complaint")
    async def complaint(self, ctx):
        """Get info on how to file a complaint against a discord member or against a member of staff."""
        try:
            if not ctx.author.dm_channel:
                await ctx.author.create_dm()
            await ctx.author.dm_channel.send(
                "To make a complaint against a regular discord member please use the ``-report <your_report_here>`` command. These reports will be seen by all staff members."
            )
            await ctx.author.dm_channel.send(
                "To make a complaint against a member of staff please use the ``-contact <your_report_here>`` command. These reports will be seen by admins."
            )
            await ctx.author.dm_channel.send("Both commands can be used in direct messages.")
        except discord.Forbidden:
            await ctx.send(
                "I could not send you a DM. Make sure I can send you a direct message due to the confidentiality of your issue."
            )

    @commands.command(name="commands")
    async def user_helper(self, ctx):
        """See all bot commands using -help"""
        await ctx.send("Use ``-help`` to see all bot commands.")

    """@commands.command()
    async def spam(self, ctx, r: int, *, text: str):
        if ctx.author.id == 428675506947227648:
            for i in range(0, r):
                i  # Stop screaming at me for not using the variable VSCode!!!!
                await ctx.send(text)
        elif ctx.author.id == 472727265713586176:
            for i in range(0, r):
                await ctx.send(
                    f"No Jackieboi you can not do that. Here, have a ping: {ctx.author.mention}"
                )
        else:
            await ctx.send(f"Nope. Evil {ctx.author.mention}.")"""

    @commands.command()
    async def amy2(self, ctx):
        await ctx.send(
            "https://cdn.discordapp.com/attachments/428677715973898270/726090406668009472/Screenshot_20200626-125925.jpg"
        )

    @commands.command()
    @checks.mod()
    async def issuereport(self, ctx):
        await ctx.send("Report all issues here: https://forms.gle/PGgi1kZ3ExrV3Kij7")

    @commands.command()
    @checks.mod()
    async def moderation(self, ctx):
        """Quick reference to moderation commands."""
        text = """```AsciiDoc
[Moderation commands]\n
-check <User>                      | Check flags, warnings and userinfo for a user.
-lvlinfo <User> | -rank <User>     | Get info about a current user's rank.
-forcenick <User> [Reason]         | Force-change a user's nickname.
-flag <User> <Reason>              | Flag a user (staff notes).
-warn <User> <Reason>              | Warn a user.
-tm <User> [Reason] --for <time>   | -tm <User> [Reason] --for 12 hours | Tempmute a user.    | Alias: -moo
-mute                              | See all muting options including voice or channel mutes.
-claw <User>                       | Put a user into the #contact-claws channel.
-return <fireteam/burning> <User>  | Return a user from the #contact-claws channel.


[Quick-access messages]\n
-admin                             | Get an admin to help you.
-bot                               | Run this if someone asks us to put a bot in.
-rp [User]                         | Run this if someone asks a ARP or otherwise RP related question.


[Other]\n
-issuereport                       | Something is broken? Report it here. Staff only.
```"""
        await ctx.send(text)
