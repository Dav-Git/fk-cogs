import discord
from sys import stderr
from redbot.core import commands, checks, Config, modlog
from typing import Optional


class Claw(commands.Cog):
    """Claw cog"""

    async def red_delete_data_for_user(self, *, requester, user_id):
        pass  # This cog stores no EUD

    def __init__(self):
        self.config = Config.get_conf(self, 889, force_registration=True)
        default_member = {"overrides": {}, "clawed": False, "channel": 0}
        self.config.register_member(**default_member)

    async def initialize(self):
        await self.register_casetypes()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 332834024831582210:
            if await self.config.member(member).clawed():
                await member.add_roles(
                    member.guild.get_role(707949167338586123), reason="Re-Clawed"
                )
                for channel in member.guild.channels:
                    new_overrides = channel.overwrites
                    new_overrides[member] = discord.PermissionOverwrite(
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
                    member.guild.default_role: discord.PermissionOverwrite(
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
                    member.guild.get_role(332835206493110272): discord.PermissionOverwrite(
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
                    member: discord.PermissionOverwrite(
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
                channel = member.guild.get_channel(await self.config.member(member).channel())
                await channel.edit(overwrites=nc_override)
                await member.guild.get_channel(449945421742211082).send(
                    f"{member.display_name}({member.id}) has been re-captured to {channel.mention}"
                )

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
    @commands.max_concurrency(1, commands.BucketType.default, wait=False)
    @checks.mod()
    async def claw(self, ctx, user: discord.Member, *, reason: Optional[str]):
        """``[Member]`` | Claw a member."""
        await user.add_roles(ctx.guild.get_role(707949167338586123), reason="Clawed")
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
        await self.config.member(user).channel.set(channel.id)
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
            reason=reason,
        )
        await self.config.member(user).clawed.set(True)
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
    @commands.max_concurrency(1, commands.BucketType.default, wait=False)
    @checks.mod()
    async def return_member(self, ctx, user: discord.Member, *, reason: str):
        """Return a member out of #contact-claws."""
        if len(reason) > 1000:
            await ctx.send("The reason for this case was to long. I will shorten it for you.")
            reason = reason[:1000]
        await ctx.send(
            "Don't panic. This will take a while. Sit back and relax as your channels are coming back."
        )
        async with ctx.typing():
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
            await user.remove_roles(ctx.guild.get_role(707949167338586123), reason="Unclawed")
            await self.config.member(user).overrides.set({})
            await modlog.create_case(
                ctx.bot,
                ctx.guild,
                ctx.message.created_at,
                action_type="unclaw",
                user=user,
                moderator=ctx.author,
                reason=reason,
            )
            await self.config.member(user).clawed.set(False)

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
