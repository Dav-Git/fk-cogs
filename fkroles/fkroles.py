from typing import Optional
import discord
from redbot.core import commands, modlog

class FKRoles(commands.Cog):

    async def red_delete_data_for_user(self, *, requester, user_id):
        pass  # This cog stores no EUD

    def __init__(self, bot):
        self.bot = bot
    
    async def initialize(self):
        await self.reg_ct()

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
            {
                "name": "nem",
                "default_setting": True,
                "image": "\N{NO ENTRY}",
                "case_str": "NEM",
            },
            {
                "name": "nsb",
                "default_setting": True,
                "image": "<CatPolice:639970673728421908>",
                "case_str": "NSB",
            }
        ]
        await modlog.register_casetypes(new_types)

    @commands.mod()
    @commands.group()
    async def punish (self,ctx):
        """Punish the user by assinging restrictive roles"""
        pass
        #await ctx.send("# Overview: \n\n1. nsp: No Self Promotion\n2. nss: No Scenario Suggestions\n3. ncc: No Creative Channels\n4. nem No Embeds\n5. nsb: No Soundboard")
        #await ctx.send("https://tenor.com/view/spank-gif-18116954")

    @punish.command(aliases=["noselfpromotion"])
    async def nsp(self, ctx, member: discord.Member, *, reason: Optional[str]):
        """Assign NSP to a member.\n\nThis role is used to block access to #self-promotion ."""
        await self.do_the_thing(ctx.guild.get_role(699776108970770542), member, "nsp", ctx, reason)
        await ctx.tick()

    @punish.command(aliases=["noscenariosuggestions"])
    async def nss(self, ctx, member: discord.Member, *, reason: Optional[str]):
        """Assign NSS to a member.\n\nThis role is used to block access to #scenario-suggestions ."""
        await self.do_the_thing(ctx.guild.get_role(672402596098736128), member, "nss", ctx, reason)
        await ctx.tick()

    @punish.command(aliases=["nocreativechannels"])
    async def ncc(self, ctx, member: discord.Member, *, reason: Optional[str]):
        """Assign NCC to a member.\n\nThis role is used to block access to creative channels."""
        await self.do_the_thing(ctx.guild.get_role(507595253814001664), member, "ncc", ctx, reason)
        await ctx.tick()

    @punish.command(aliases=["noembeds"])
    async def nem(self,ctx, member: discord.Member,* , reason: Optional[str]):
        """Assing NEM to a member. This role is used to block embeds from the user."""
        await self.do_the_thing(ctx.guild.get_role(1228617211866906706), member, "nem", ctx, reason)
        await ctx.tick()

    @punish.command(aliases=["nosoundboard"])
    async def nsb(self,ctx, member: discord.Member, *, reason:Optional[str]):
        """Assign NSB to a member. This role is used to deny soundboard perms."""


    async def do_the_thing(self,role: discord.Role, member:discord.Member,case_str:str, ctx, reason:str)->None:
        """Does the thing."""
        await member.add_roles(role)
        await modlog.create_case(
            ctx.bot,
            ctx.guild,
            ctx.message.created_at,
            role.name,
            case_str,
            ctx.author,
            reason if reason else None,
        )    

    @commands.mod()
    @commands.command()
    async def bd(self, ctx, member: discord.Member):
        """Toggle the bday role on a member."""
        role = ctx.guild.get_role(657943577065947157)
        if role in member.roles:
            await member.remove_roles(role)
            await ctx.tick()
        else:
            await member.add_roles(role)
            await ctx.tick()