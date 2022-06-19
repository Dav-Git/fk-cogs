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

    async def initialize(self):
        await self.reg_ct()

    @tasks.loop(minutes=2, count=1)
    async def uwu_image_task(self):
        await self.bot.wait_until_red_ready()
        await self.bot.get_guild(332834024831582210).get_channel(332834024831582210).send(
            "https://imgur.com/a/lPYyplA"
        )

    @staticmethod
    async def reg_ct():
        new_types = [
            {
                "name": "nsp",
                "default_setting": True,
                "image": "<a:bonk_newspaper_bean:736744548138745866>",
                "case_str": "NSP",
            },
            {
                "name": "nss",
                "default_setting": True,
                "image": "\N{OPEN BOOK}",
                "case_str": "NSS",
            },
            {
                "name": "ncc",
                "default_setting": True,
                "image": "\N{ARTIST PALETTE}",
                "case_str": "NCC",
            },
        ]
        await modlog.register_casetypes(new_types)

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
            "{}\nFeeling like you or someone you know needs help?  Please visit https://checkpointorg.com/global/  They have resources help you and can give advice or guide you in the right direction.".format(
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

    @checks.admin()
    @commands.command()
    async def nsp(self, ctx, member: discord.Member, *, reason: Optional[str]):
        """Assign NSP to a member.\n\nThis role is used to block access to #self-promotion ."""
        await member.add_roles(ctx.guild.get_role(699776108970770542))
        await modlog.create_case(
            ctx.bot,
            ctx.guild,
            ctx.message.created_at,
            "nsp",
            member,
            ctx.author,
            reason if reason else None,
        )
        await ctx.tick()

    @checks.admin()
    @commands.command()
    async def nss(self, ctx, member: discord.Member, *, reason: Optional[str]):
        """Assign NSS to a member.\n\nThis role is used to block access to #scenario-suggestions ."""
        await member.add_roles(ctx.guild.get_role(672402596098736128))
        await modlog.create_case(
            ctx.bot,
            ctx.guild,
            ctx.message.created_at,
            "nss",
            member,
            ctx.author,
            reason if reason else None,
        )
        await ctx.tick()

    @checks.admin()
    @commands.command()
    async def ncc(self, ctx, member: discord.Member, *, reason: Optional[str]):
        """Assign NCC to a member.\n\nThis role is used to block access to creative channels."""
        await member.add_roles(ctx.guild.get_role(507595253814001664))
        await modlog.create_case(
            ctx.bot,
            ctx.guild,
            ctx.message.created_at,
            "ncc",
            member,
            ctx.author,
            reason if reason else None,
        )
        await ctx.tick()

    @commands.mod()
    @commands.command()
    async def faq(self, ctx, member: Optional[discord.Member] = None):
        """Get a link to the FAQ."""
        await ctx.send(
            f"{member.mention if member else ''} Hey there, this question has already been answered in our faqs channel. Please have a look in that channel for your answer, thanks."
        )

    @commands.command(name="commands")
    async def user_helper(self, ctx):
        """See all bot commands using -help"""
        await ctx.send("Use ``-help`` to see all bot commands.")

    @commands.command(aliases=["issuereport"])
    @checks.mod()
    async def moderation(self, ctx):
        """Quick reference to moderation commands."""
        em = discord.Embed(
            title="Moderation Commands",
            description="Listed below is a quickhand list of common commands, their uses, and special requirements (if applicable).",
        )
        em.add_field(
            inline=False,
            name="**-check [UID]**",
            value="Checks a given user's warns, mutes, kicks, bans, flags and userinfo.",
        )
        em.add_field(
            inline=False,
            name="**-freezenick [UID] [Nickname] [Reason]**",
            value="Freezes the nickname of the user to a selected name.",
        )
        em.add_field(
            inline=False,
            name="**-flag [UID] [Reason]**",
            value="Logs a flag onto a user. Useful for things that aren't warn worthy but should still be noted (think of a notepad for each user).",
        )
        em.add_field(
            inline=False,
            name="**-joinflag [UID] [Reason]**",
            value="Adds a flag onto a user that will be displayed when they rejoin the server.",
        )
        em.add_field(
            inline=False,
            name="**-warn [UID] [Points - Optional, Default 1] [Reason]**",
            value="Issues a warning to the user. Will send a DM to them if they can receive DMs.",
        )
        em.add_field(
            inline=False,
            name="**-mute [UID] [Duration] [Reason]**",
            value="Mutes a user for a given time frame. If no duration is noted, the mute will permanent.",
        )
        em.add_field(
            inline=False,
            name="**-claw [UID] [Reason]**",
            value="Brings the user into a private channel that only staff are able to see. This is for moderation use cases and will remove all other channels from view.",
        )
        em.add_field(
            inline=False,
            name="**-softclaw [UID]**",
            value="Brings the user into a private channel that only staff are able to see. This is for lighter use cases such as providing help, does not remove all other channels from view.",
        )
        em.add_field(
            inline=False,
            name="**-return [UID]**",
            value="Returns a user out of a claw or softclaw.",
        )
        em.add_field(
            inline=False,
            name="**-rp [UID - Optional]**",
            value="Create an automated message that redirects a user to the ask-rp-info channel.",
        )
        em.add_field(
            inline=False,
            name="**-faq [UID - Optional]**",
            value="Creates an automated message that redirects a user to the faqs channel.",
        )
        em.add_field(inline=False, name="**-admin**", value="Summons an admin to the channel.")
        em.add_field(inline=False, name="**-mod**", value="Summons a mod to the channel.")
        em.add_field(
            inline=False,
            name="**-bug [Title - Put in Quotes] [Priority 1 (low) - 3 (high)] [Text]**",
            value="Creates a bug report on our GitHub page that Dan and Dav will investigate (eventually).",
        )
        em.add_field(
            inline=False,
            name="**-feature [Title - Put in Quotes] [Text]**",
            value="Creates a feature request on the GitHub that Dav and Dan might eventually look at (this is the same formatting for -enhancement).",
        )
        em.add_field(
            inline=False,
            name="**-blocklist add [UID]**",
            value="Blocks a user from being able to use the bot.",
        )
        em.color = 0x923EDB
        await ctx.send(embed=em)
