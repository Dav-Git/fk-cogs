from typing import Optional
import discord
from discord.ext import tasks
from redbot.core import checks, commands, modlog


class FKCom(commands.Cog):
    async def red_delete_data_for_user(self, *, requester, user_id):
        pass  # This cog stores no EUD

    def __init__(self, bot):
        self.bot = bot
        self.uwu_image_task.start()

    @tasks.loop(minutes=2, count=1)
    async def uwu_image_task(self):
        await self.bot.wait_until_red_ready()
        await self.bot.get_guild(332834024831582210).get_channel(332834024831582210).send(
            "https://imgur.com/a/lPYyplA"
        )

    

    @commands.command()
    async def rp(self, ctx, user: Optional[discord.User], channel: Optional[discord.TextChannel]):
        """Blanket warn message for rp questions"""
        if not channel:
            channel = ctx.channel
        await channel.send(
            "Hey{}, it seems like you have asked a question about ARP (Aspirant Gaming). We are not affiliated with ARP at all and sadly can not provide any information to you. To receive an answer to your question, try {} or the Aspirant Gaming discord server.".format(
                " " + user.mention if user != None else "\u200b",
                ctx.guild.get_channel(478917077705555970).mention,
            )
        )

    @commands.command()
    async def mh(self, ctx, user: Optional[discord.Member]):
        """Mental health advisory"""
        await ctx.send(
            """{}\nWe sadly cannot provide detailed and dedicated support for mental health issues. If you or someone you know is struggling mentally, please look at the following links for guidance and support.

**United Kingdom**
*Mind's Recommended Resources*
- <https://www.mind.org.uk/information-support/types-of-mental-health-problems/suicidal-feelings/useful-contacts/>
- <https://www.mind.org.uk/information-support/types-of-mental-health-problems/depression/useful-contacts/>

**United States**
*Mental Health America*
- <https://www.mhanational.org/resources/988>
*CDC*
- <https://www.cdc.gov/suicide/index.html>
*National Institute of Mental Health*
- <https://www.nimh.nih.gov/health/find-help>

**International**
- <https://www.iasp.info/suicidalthoughts/>""".format(
                user.mention if user != None else "\u200b"
            )
        )

    @commands.command(name="staff")
    async def get_mod_attention(self, ctx, *, details: Optional[str]):
        """Get a moderator to help you."""
        modrolestr = ctx.guild.get_role(775359048342044713).mention
        await ctx.send(
            "A {} has been requested.".format(
                ctx.guild.get_role(332835206493110272).mention,
            )
        )
        await ctx.guild.get_channel(339741123406725121).send(
            "A {} has been requested in {}.{}".format(
                modrolestr, ctx.channel.mention, f"\n``{details}``" if details else ""
            ),
            allowed_mentions=discord.AllowedMentions(roles=True),
        )

    @commands.command(name="admin")
    async def get_admin_attention(self, ctx):
        """Get an admin to help you."""
        adminrolestr = ctx.guild.get_role(775332588196724767).mention
        await ctx.send(
            "An {} has been requested.".format(ctx.guild.get_role(332834961407213568).mention)
        )
        await ctx.guild.get_channel(360478963115491328).send(
            "An {} has been requested in {}.".format(adminrolestr, ctx.channel.mention),
            allowed_mentions=discord.AllowedMentions(roles=True),
        )

    @commands.mod()
    @commands.command()
    async def faq(self, ctx, member: Optional[discord.Member] = None):
        """Get a link to the FAQ."""
        await ctx.send(
            f"{member.mention if member else ''} Hey there, this question has already been answered in our {ctx.guild.get_channel(661012030081204257).mention} channel. Please have a look in that channel for your answer, thanks."
        )

    @commands.command(name="commands")
    async def user_helper(self, ctx):
        """See all bot commands using -help"""
        await ctx.send("Use ``-help`` to see all bot commands.")

    @commands.command()
    @checks.mod()
    async def modfull(self, ctx):
        """A more expanded list of commonly used moderation commands."""
        em = discord.Embed(
            title="Moderation Commands",
            description="Listed below is a quickhand list of common commands, their uses, and special requirements (if applicable)."
        )
        em.add_field(
            inline=False,
            name="**__Moderation__**",
            value=""
        )
        em.add_field(
            inline=False,
            name="**-check [UID]**",
            value="Checks a given user's warns, mutes, kicks, bans, flags and userinfo."
        )
        em.add_field(
            inline=False,
            name="**-userinfo [UID]**",
            value="Shows the user's info sheet (beginning of a check command)."
        )
        em.add_field(
            inline=False,
            name="**-flag [UID] [Reason]**",
            value="Logs a flag onto a user. Useful for things that aren't warn worthy but should still be noted (think of a notepad for each user)."
        )
        em.add_field(
            inline=False,
            name="**-warn [UID] [Points - Optional, Default 1] [Reason]**",
            value="Issues a warning to the user. Will send a DM to them if they can receive DMs."
        )
        em.add_field(
            inline=False,
            name="**-mute [UID] [Duration] [Reason]**",
            value="Mutes a user for a given time frame. If no duration is noted, the mute will permanent."
        )
        em.add_field(
            inline=False,
            name="**-alt mark [Main UID] [Alt UID]**",
            value="Notes that a member has an alt account - this will show up in checks."
        )
        em.add_field(
            inline=False,
            name="**-freezenick [UID] [Nickname] [Reason]**",
            value="Freezes the nickname of the user to a selected name."
        )
        em.add_field(
            inline=False,
            name="**-joinflag [UID] [Reason]**",
            value="Adds a flag onto a user that will be displayed when they rejoin the server."
        )
        em.add_field(
            inline=False,
            name="**-flaglist [UID]**",
            value="Shows the flags that a user has (final part of a check command)."
        )
        em.add_field(
            inline=False,
            name="**-punish [Sublevel] [UID] [Reason]**",
            value="Assigns a role to a member who abuses certain privileges (such as revoking self-promotion). Note: Manual removal can only be done by Admins."
        )
        em.add_field(
            inline=False,
            name="**-mlentries <UID>**",
            value="Counts how many modlog entries a certain member has within the server."
        )
        em.add_field(
            inline=False,
            name="**-pingsafe**",
            value="Toggles Staff pingsafe role. Can also use `-ps`"
        )
        em.add_field(
            inline=False,
            name="**__Private Channels__**",
            value=""
        )
        em.add_field(
            inline=False,
            name="**-claw [UID] [Reason]**",
            value="Brings the user into a private channel that only staff are able to see. This is for moderation use cases and will remove all other channels from view."
        )
        em.add_field(
            inline=False,
            name="**-softclaw [UID]**",
            value="Brings the user into a private channel that only staff are able to see. This is for lighter use cases such as providing help, does not remove all other channels from view."
        )
        em.add_field(
            inline=False,
            name="**-return [UID]**",
            value="Returns a user out of a claw or softclaw."
        )
        em.add_field(
            inline=False,
            name="**__Member Assist__**",
            value=""
        )
        em.add_field(
            inline=False,
            name="**-bd [UID]**",
            value="Toggles the birthday role on a member."
        )
        em.add_field(
            inline=False,
            name="**-mc [UID]**",
            value="Adds the Music-Controller role to a member."
        )
        em.add_field(
            inline=False,
            name="**-faq [UID - Optional]**",
            value="Creates an automated message that redirects a user to the faqs channel."
        )
        em.add_field(
            inline=False,
            name="**-rp [UID - Optional]**",
            value="Create an automated message that redirects a user to the ask-rp-info channel."
        )
        em.add_field(
            inline=False,
            name="**__DTT Reporting__**",
            value=""
        )
        em.add_field(
            inline=False,
            name="**-bug [Title - Put in Quotes] [Priority 1 (low) - 3 (high)] [Text]**",
            value="Creates a bug report on our GitHub page that Dan and Dav will investigate (eventually)."
        )
        em.add_field(
            inline=False,
            name="**-enhancement [Title - Put in Quotes] [Text]**",
            value="Use this format with 'feature' if you are attempting to suggest a new feature. Creates a ehnancement/feature request on the GitHub that Dav and Dan might eventually look at."
        )
        em.color=0x923EDB
        await ctx.send(embed=em)

    @commands.command()
    @checks.mod()
    async def modshort(self, ctx):
        """A condensed list of commonly used moderation commands."""
        em = discord.Embed(
            title="Quick Moderation Commands",
            description="This is a condensed list of important commands that moderators and admins will use on a regular basis."
        )
        em.add_field(
            inline=False,
            name="**-check [UID]**",
            value="Checks a given user's warns, mutes, kicks, bans, flags and userinfo."
        )
        em.add_field(
            inline=False,
            name="**-flag [UID] [Reason]**",
            value="Logs a flag onto a user. Useful for things that aren't warn worthy but should still be noted (think of a notepad for each user)."
        )
        em.add_field(
            inline=False,
            name="**-warn [UID] [Points - Optional, Default 1] [Reason]**",
            value="Issues a warning to the user. Will send a DM to them if they can receive DMs."
        )
        em.add_field(
            inline=False,
            name="**-mute [UID] [Duration] [Reason]**",
            value="Mutes a user for a given time frame. If no duration is noted, the mute will permanent.")
        em.add_field(
            inline=False,
            name="**-claw [UID] [Reason]**",
            value="Brings the user into a private channel that only staff are able to see. This is for moderation use cases and will remove all other channels from view."
        )
        em.add_field(
            inline=False,
            name="**-return [UID]**",
            value="Returns a user out of a claw or softclaw."
        )
        em.add_field(
            inline=False,
            name="**-bd [UID]**",
            value="Toggles the birthday role on a member."
        )
        em.add_field(
            inline=False,
            name="**-faq [UID - Optional]**",
            value="Creates an automated message that redirects a user to the faqs channel."
        )
        em.add_field(
            inline=False,
            name="**-rp [UID - Optional]**",
            value="Create an automated message that redirects a user to the ask-rp-info channel."
        )
        em.add_field(
            inline=False,
            name="**-bug [Title - Put in Quotes] [Priority 1 (low) - 3 (high)] [Text]**",
            value="Creates a bug report on our GitHub page that Dan and Dav will investigate (eventually)."
        )
        em.color=0x923EDB
        await ctx.send(embed=em)

    @commands.command()
    async def fakemod(self, ctx):
        """A list of troll moderation commands."""
        em = discord.Embed(title="Moderation Commands",description="Is only joke")
        em.add_field(
            inline=False,
            name="**-bam [User] [Reason]**",
            value="Bammity bam bam!"
        )
        em.add_field(
            inline=False,
            name="**-kik [User] [Reason]**",
            value="Kik 'em to the moon!"
        )
        em.add_field(
            inline=False,
            name="**-myut [User] [Reason]**",
            value="Myut the noot."
        )
        em.add_field(
            inline=False,
            name="**-worn [User] [Reason]**",
            value="Worn them to the warth."
        )
        em.set_footer(
            text="Our Laywer has advised us to denote that 'This is soley a joke for the meme-ery and should not be taken seriously.'\nAnd our Admin Overlords have requested 'Please do not abuse this - especially if someone has asked you to stop.'"
        )
        em.color=0x29D6A8
        await ctx.send(embed=em)
    
    @commands.mod()
    @commands.command()
    async def rules(self, ctx, member: Optional[discord.Member] = None):
        """Send the rules channel to someone."""
        # Thanks Dan
        await ctx.send(
            f"{member.mention if member else ''} Please take a look at the {ctx.guild.get_channel(478954069189459998).mention} channel. Please keep in mind some channels have rules specific to the channel so remember to check the pins!"
        )

    @commands.mod()
    @commands.command()
    async def mlentriestd(self,ctx):
        """How many ModLog entries does TesterDan have?"""
        await ctx.send(f"Tester Dan has {len(await modlog.get_cases_for_member(bot=ctx.bot,guild=ctx.guild,member_id=481802382251130906))} ModLog entries.")

    @commands.mod()
    @commands.command()
    async def mlentries(self,ctx,member: discord.Member):
        """How many ModLog entries does a member have?"""
        await ctx.send(f"{member} has {len(await modlog.get_cases_for_member(bot=ctx.bot,guild=ctx.guild,member_id=member.id))} ModLog entries.")
        
