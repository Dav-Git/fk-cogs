from redbot.core import commands, Config
import discord


class OneTimeMessage(commands.Cog):
    def __init__(self):
        self.config = Config.get_conf(self, identifier=161605022021, force_registration=True)
        self.config.register_member(channels=[])
        self.config.register_channel(text=None, roles=[])

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if (not message.guild) or message.author.bot:
            return
        text = await self.config.channel(message.channel).text()
        if text:
            roles = await self.config.channel(message.channel).roles()
            for role in roles:
                if role in [x.id for x in message.author.roles]:
                    async with self.config.member(message.author).channels() as channels:
                        if message.channel.id in channels:
                            return
                        else:
                            try:
                                await message.author.send(
                                    text.format(
                                        user=message.author,
                                        guild=message.guild,
                                        channel=message.channel,
                                    )
                                )
                            except discord.Forbidden:
                                pass
                            channels.append(message.channel.id)

    @commands.admin()
    @commands.group()
    async def otm(self, ctx):
        """One time messages settings."""
        pass

    @otm.command()
    async def message(self, ctx, channel: discord.TextChannel, *, text: str):
        """Add a one time message to a channel.\n\nYou can use `{user}`, `{guild}`and `{channel} to customize your message.`"""
        await self.config.channel(channel).text.set(text)
        await ctx.send(f"Message set to:\n{text}")

    @otm.command()
    async def clearmessage(self, ctx, channel: discord.TextChannel):
        """Remove the one time message from a channel."""
        await self.config.channel(channel).text.set(None)
        await ctx.send("Message cleared")

    @otm.command()
    async def addrole(self, ctx, channel: discord.TextChannel, role: discord.Role):
        """Add a role to a one time message channel."""
        async with self.config.channel(channel).roles() as roles:
            roles.append(role.id)
        await ctx.send(f"{role.name} added to {channel.name}.")

    @otm.command()
    async def removerole(self, ctx, channel: discord.TextChannel, role: discord.Role):
        """Remove a role from a one time message channel."""
        async with self.config.channel(channel).roles() as roles:
            try:
                roles.remove(role.id)
                await ctx.send(f"{role.name} removed from {channel.name}.")
            except ValueError:
                await ctx.send("Role was not a part of the channel.")

    @otm.command()
    async def clearrole(self, ctx, channel: discord.TextChannel):
        """Clear all roles from a one time message channel."""
        await self.config.channel(channel).roles.set([])
        await ctx.send("Roles cleared.")

    @otm.command()
    async def clearmem(self, ctx, channel: discord.TextChannel):
        async with self.config.member(ctx.author).channels() as channels:
            try:
                channels.remove(channel.id)
            except ValueError:
                pass
        await ctx.tick()