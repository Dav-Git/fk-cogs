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
            "http://stopdavabuse.de/dl/dc8.png"
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
            "{}\nFeeling like you or someone you know needs help or a place to vent some negative feelings and don't know where to start?  Please visit The Mental Health Together Discord.  They have resources help you and can give advice or guide you in the right direction. The server has areas to vent, share your story and get in touch with others.  There are also some fun areas to share hobbies like food, cute animal pics, etc.\n\nPlease feel free to visit or invite your friends with this link: <https://discord.mhtogether.com/>".format(
                user.mention if user != None else "\u200b"
            )
        )

    @commands.command(name="staff")
    async def get_mod_attention(self, ctx, *, details: Optional[str]):
        """Get a moderator to help you."""
        modrolestr = ctx.guild.get_role(775359048342044713).mention
        await ctx.send("A {} has been requested.".format(modrolestr))
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
        await ctx.send("An {} has been requested.".format(adminrolestr))
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

    @commands.command(name="commands")
    async def user_helper(self, ctx):
        """See all bot commands using -help"""
        await ctx.send("Use ``-help`` to see all bot commands.")

    @commands.command(aliases=["issuereport"])
    @checks.mod()
    async def moderation(self, ctx):
        """Quick reference to moderation commands."""
        text = """```AsciiDoc
[Moderation commands]\n
-check <User>                          | Check flags, warnings and userinfo for a user.
-lvlinfo <User> | -rank <User>         | Get info about a current user's rank.
-forcenick <User> [Reason]             | Force-change a user's nickname.
-flag <User> <Reason>                  | Flag a user (staff notes).
-joinflag <UserID> <text>              | Add a text which is shown when a user (re-)joins the server.
-warn <User> <Reason>                  | Warn a user.
-mute <User> [duration] [Reason]       | Mute a user. Provide a duration to make it a tempmute. 
-channelmute <User> [duration] [Reason]| Mute a user in a channel.
-voicemute <User> [Reason]             | Mute a user in a voicechannel.
-voiceban                              | Ban a user from all voicechannels.
-activemutes                           | See all curently active mutes.
-claw <User> <Reason>                  | Put a user into the #contact-claws channel. Requires descriptive reason.
-return <User>                         | Return a user from the #contact-claws channel.


[Quick-access messages]\n
-admin                             | Get an admin to help you.
-bot                               | Run this if someone asks us to put a bot in.
-rp [User]                         | Run this if someone asks a ARP or otherwise RP related question.


[Other]\n
-bug <Title> [Priority 1-3] <Text>         | Something is broken? Report it here. Staff only.
-enhancement <Title> [Priority 1-3] <Text> | You have an idea on how to do something better? Put it here. Staff only.
-feature <Title> [Priority 1-3] <Text>     | You have a new feature idea? This is your command. Staff only.
 ! IMPORTANT: If your title consists of more than one word make sure to wrap it in quotes. "This title"
              The default priority is 1/low.
-blocklist add <User>                       | Block a user from interacting with the bot. Permission only.
```"""
        await ctx.send(text)
