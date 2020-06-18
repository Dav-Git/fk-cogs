import discord
from sys import stderr
from redbot.core import commands, checks, Config, modlog


class Claw(commands.Cog):
    """Claw cog"""

    def __init__(self):
        self.config = Config.get_conf(self, 889, force_registration=True)
        default_member = {"overrides": {}}
        self.config.register_member(**default_member)

    async def initialize(self):
        await self.register_casetypes()

    @staticmethod
    async def register_casetypes():
        cases = [
            {
                "name": "claw",
                "default_setting": True,
                "image": "\N{POLICE OFFICER}",
                "case_str": "Clawed",
            },
            {
                "name": "unclaw",
                "default_setting": True,
                "image": "<a:Party_cat:639970674940575764>",
                "case_str": "Returned",
            },
        ]
        await modlog.register_casetypes(cases)

    @commands.command()
    @checks.mod()
    async def claw(self, ctx, user: discord.Member):
        """``[Member]`` | Claw a member."""
        async with self.config.member(user).overrides() as overrides:
            for channel in ctx.guild.channels:
                if user in channel.overwrites:
                    overrides[channel.id] = dict(channel.overwrites[user])
                new_overrides = channel.overwrites
                new_overrides[user] = discord.PermissionOverwrite(
                    external_emojis=False,
                    read_message_history=False,
                    view_guild_insights=False,
                    priority_speaker=False,
                    manage_guild=False,
                    send_tts_messages=False,
                    manage_messages=False,
                    connect=False,
                    attach_files=False,
                    send_messages=False,
                    administrator=False,
                    speak=False,
                    manage_webhooks=False,
                    read_messages=False,
                    change_nickname=False,
                    create_instant_invite=False,
                    use_voice_activation=False,
                    add_reactions=False,
                    move_members=False,
                    manage_emojis=False,
                    stream=False,
                    embed_links=False,
                    view_audit_log=False,
                    manage_nicknames=False,
                    kick_members=False,
                    deafen_members=False,
                    manage_roles=False,
                    mention_everyone=False,
                    ban_members=False,
                    mute_members=False,
                    manage_channels=False,
                )
                await channel.edit(overwrites=new_overrides)
        nc_override = {
            ctx.guild.default_role: discord.PermissionOverwrite(
                external_emojis=False,
                read_message_history=False,
                view_guild_insights=False,
                priority_speaker=False,
                manage_guild=False,
                send_tts_messages=False,
                manage_messages=False,
                connect=False,
                attach_files=False,
                send_messages=False,
                administrator=False,
                speak=False,
                manage_webhooks=False,
                read_messages=False,
                change_nickname=False,
                create_instant_invite=False,
                use_voice_activation=False,
                add_reactions=False,
                move_members=False,
                manage_emojis=False,
                stream=False,
                embed_links=False,
                view_audit_log=False,
                manage_nicknames=False,
                kick_members=False,
                deafen_members=False,
                manage_roles=False,
                mention_everyone=False,
                ban_members=False,
                mute_members=False,
                manage_channels=False,
            ),
            ctx.guild.get_role(332835206493110272): discord.PermissionOverwrite(
                external_emojis=True,
                read_message_history=True,
                view_guild_insights=False,
                priority_speaker=False,
                manage_guild=False,
                send_tts_messages=False,
                manage_messages=True,
                connect=False,
                attach_files=True,
                send_messages=True,
                administrator=False,
                speak=False,
                manage_webhooks=False,
                read_messages=True,
                change_nickname=False,
                create_instant_invite=False,
                use_voice_activation=False,
                add_reactions=True,
                move_members=False,
                manage_emojis=False,
                stream=False,
                embed_links=True,
                view_audit_log=False,
                manage_nicknames=False,
                kick_members=False,
                deafen_members=False,
                manage_roles=False,
                mention_everyone=False,
                ban_members=False,
                mute_members=False,
                manage_channels=False,
            ),
            user: discord.PermissionOverwrite(
                external_emojis=True,
                read_message_history=True,
                view_guild_insights=False,
                priority_speaker=False,
                manage_guild=False,
                send_tts_messages=False,
                manage_messages=False,
                connect=False,
                attach_files=True,
                send_messages=True,
                administrator=False,
                speak=False,
                manage_webhooks=False,
                read_messages=True,
                change_nickname=False,
                create_instant_invite=False,
                use_voice_activation=False,
                add_reactions=True,
                move_members=False,
                manage_emojis=False,
                stream=False,
                embed_links=True,
                view_audit_log=False,
                manage_nicknames=False,
                kick_members=False,
                deafen_members=False,
                manage_roles=False,
                mention_everyone=False,
                ban_members=False,
                mute_members=False,
                manage_channels=False,
            ),
        }
        channel = await ctx.guild.create_text_channel(
            name=f"contact-{user.name}",
            overwrites=nc_override,
            category=ctx.guild.get_channel(360775964470280193),
            reason=f"{user.name}#{user.discriminator} has been clawed.",
        )
        await channel.send(
            f"Hello {user.mention}, you have been pulled into the contact area, a member of staff will be with you shortly."
        )
        await modlog.create_case(
            ctx.bot,
            ctx.guild,
            ctx.message.created_at,
            action_type="claw",
            user=user,
            moderator=ctx.author,
        )
        """try:
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
            )"""

    @commands.command(name="return")
    @checks.mod()
    async def return_member(self, ctx, user: discord.Member):
        """Return a member out of #contact-claws."""
        settings = await self.config.member(user).overrides()
        for channel in ctx.guild.channels:
            new_overrides = channel.overwrites
            try:
                del new_overrides[user]
            except KeyError:
                pass
            try:
                new_overrides[user] = discord.PermissionOverwrite(**settings[channel.id])
            except KeyError:
                pass
            await channel.edit(overwrites=new_overrides)
        await self.config.member(user).overrides.set({})
        await modlog.create_case(
            ctx.bot,
            ctx.guild,
            ctx.message.created_at,
            action_type="unclaw",
            user=user,
            moderator=ctx.author,
        )

    """@return_member.command()
    async def fireteam(self, ctx, user: discord.Member):
        
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

    @return_member.command(aliases=["basic", "normal", "everyone", "nobody"])
    async def standard(self, ctx, user: discord.Member):
        
        if ctx.guild.get_role(483212257237401621) in user.roles:
            await user.remove_roles(
                ctx.guild.get_role(483212257237401621), reason="Returned from Contact claws."
            )
            await ctx.guild.get_channel(350726339327950859).send(
                f"{user.name} has been returned from {ctx.guild.get_channel(483213085293936640).mention}."
            )"""
