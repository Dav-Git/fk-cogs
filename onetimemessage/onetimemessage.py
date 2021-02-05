from redbot.core import commands, Config
import discord


class OneTimeMessage(commands.Cog):
    def __init__(self):
        self.config = Config.get_conf(self, identifier=161605022021, force_registration=True)
        self.config.register_member(channels=[])
        self.config.register_channel(text=None)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if (not message.guild) or message.author.bot:
            return
        text = await self.config.channel(message.channel).text()
        if text:
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

    @commands.command()
    async def otm(self, ctx, channel: discord.TextChannel, *, text: str):
        """Add a one time message to a channel.\n\nYou can use `{user}`, `{guild}`and `{channel} to customize your message.`"""
        await self.config.channel(channel).text.set(text)
        await ctx.send(f"Message set to:\n{text}")

    @commands.command()
    async def cotm(self, ctx, channel: discord.TextChannel):
        """Remove the one time message from a channel."""
        await self.config.channel(channel).text.set(None)
        await ctx.send("Message cleared")