from datetime import datetime, timedelta, timezone
from sys import stderr
from typing import Optional

import discord
from redbot.core import checks, commands


class FKCom(commands.Cog):
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        # Welcome to YT-Members
        if before.guild.get_role(699653447561117697) in after.roles:
            if not before.guild.get_role(699653447561117697) in before.roles:
                await after.guild.get_channel(697117977308430356).send(
                    f"Welcome to the YouTube channel members chat {after.mention}!"
                )
        # Welcome to Nitro boosters
        if before.guild.get_role(586310188135481375) in after.roles:
            if not before.guild.get_role(586310188135481375) in before.roles:
                await after.guild.get_channel(699766264784093255).send(
                    f"Welcome to the Nitro-Booster chat {after.mention}!"
                )
        # Remove burning if dot is present
        if after.guild.get_role(498528746123427851) in after.roles:
            if after.guild.get_role(489455280266936321) in after.roles:
                await after.remove_roles(after.guild.get_role(489455280266936321))
                await after.add_roles(after.guild.get_role(634692203582717990))

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        # Show #no-mic if member in VC
        if after.channel:
            if after.channel.id in [332834234135740416, 518130862492090415, 481820769568161793]:
                overwrite = discord.PermissionOverwrite()
                overwrite.send_messages = True
                overwrite.read_messages = True
                await member.guild.get_channel(702969795389292584).set_permissions(
                    member, overwrite=overwrite
                )
            else:
                await member.guild.get_channel(702969795389292584).set_permissions(
                    member, overwrite=None
                )
        else:
            await member.guild.get_channel(702969795389292584).set_permissions(
                member, overwrite=None
            )
        # Expand VC if more than 3 staff inside
        staffcounter = 0
        if after.channel:
            channelref = after.channel
        elif before.channel:
            channelref = before.channel
        mems = channelref.members
        staffroles = (
            channelref.guild.get_role(530016413616963591),
            channelref.guild.get_role(332835206493110272),
            channelref.guild.get_role(344440746264231936),
            channelref.guild.get_role(332834961407213568),
        )
        for m in mems:
            for r in staffroles:
                if r in m.roles:
                    staffcounter += 1
        if staffcounter > 2 and staffcounter < 6:
            await channelref.edit(user_limit=15, reason="3+ Staff in channel.")
        elif staffcounter > 5:
            await channelref.edit(user_limit=20, reason="6+ Staff in channel.")
        else:
            await channelref.edit(user_limit=10, reason="Fewer than 3 Staff in channel.")

    # Mod-tools
    @commands.command()
    @checks.mod()
    async def claw(self, ctx, user: discord.Member):
        """``[Member]`` | Puts a member into #contact-claws."""
        roles = {
            "fireteam": ctx.guild.get_role(634692203582717990),
            "burning": ctx.guild.get_role(489455280266936321),
            "contact": ctx.guild.get_role(483212257237401621),
        }
        try:
            if roles["fireteam"] in user.roles:
                await user.remove_roles(roles["fireteam"], reason="Contact claws assigned.")
            elif roles["burning"] in user.roles:
                await user.remove_roles(roles["burning"], reason="Contact claws assigned.")
            await user.add_roles(roles["contact"], reason="Contact claws assigned.")
            await ctx.guild.get_channel(350726339327950859).send(
                f"{user.name} has been put into {ctx.guild.get_channel(483213085293936640).mention}."
            )
            print(
                f"{ctx.author.name}({ctx.author.id}) clawed {user.name}({user.id}).", file=stderr
            )
        except:
            await ctx.send("An error occured.")
            print(
                f"{ctx.author.name}({ctx.author.id}) tried to claw {user.name}({user.id}) but something went wrong.",
                file=stderr,
            )

    @commands.group(name="return")
    @checks.mod()
    async def return_member(self, ctx):
        """Return a member out of #contact-claws. Use ``fireteam`` or ``burning`` to decide at which level they re-join the conversation."""
        pass

    @return_member.command()
    async def fireteam(self, ctx, user: discord.Member):
        """Return them as a member of the Fireteam"""
        if ctx.guild.get_role(483212257237401621) in user.roles:
            await user.remove_roles(
                ctx.guild.get_role(483212257237401621), reason="Returned from Contact claws."
            )
            await user.add_roles(
                ctx.guild.get_role(634692203582717990), reason="Returned from Contact claws."
            )
            await ctx.guild.get_channel(350726339327950859).send(
                f"{user.name} has been returned from {ctx.guild.get_channel(483213085293936640).mention}."
            )

    @return_member.command()
    async def burning(self, ctx, user: discord.Member):
        """Return them as a Burning Bright"""
        if ctx.guild.get_role(483212257237401621) in user.roles:
            await user.remove_roles(
                ctx.guild.get_role(483212257237401621), reason="Returned from Contact claws."
            )
            await user.add_roles(
                ctx.guild.get_role(489455280266936321), reason="Returned from Contact claws."
            )
            await ctx.guild.get_channel(350726339327950859).send(
                f"{user.name} has been returned from {ctx.guild.get_channel(483213085293936640).mention}."
            )

    # Member executable

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

    @commands.command()
    async def spam(self, ctx, r: int, *, text: str):
        """Spam a channel."""
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
            await ctx.send(f"Nope. Evil {ctx.author.mention}.")

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
-check [User]                      | Check flags, warnings and userinfo for a user.
-lvlinfo [User] | -rank [User]     | Get info about a current user's rank.
-flag [User] [Reason]              | Flag a user (staff notes)
-warn [User] [Reason]              | Warn a user
-tm [User] [Reason] --for [time]   | -tm [User] [Reason] --for 12 hours | Tempmute a user.
-mute                              | See all muting options including voice or channel mutes.
-claw [User]                       | Put a user into the #contact-claws channel.
-return [fireteam/burning] [User]  | Return a user from the #contact-claws channel.


[Quick-access messages]\n
-admin                             | Get an admin to help you.
-bot                               | Run this if someone asks us to put a bot in.
-rp [User]                         | Run this if someone asks a ARP or otherwise RP related question.


[Other]\n
-issuereport                       | Something is broken? Report it here. Staff only.
```"""
        await ctx.send(text)
