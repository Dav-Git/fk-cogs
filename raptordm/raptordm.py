import discord
from redbot.core import commands, checks


class RaptorDM(commands.Cog):
    async def red_delete_data_for_user(self, *, requester, user_id):
        pass  # This cog stores no EUD

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="message")
    @checks.admin()
    async def send_pm(self, ctx, user: discord.User, *, text: str):
        try:
            await user.send(text)
            await ctx.guild.get_channel(800708255194021918).send(
                f"Outbound message from {ctx.author.mention} to {user}({user.id}):\n{text}"
            )
            if ctx.message.attachments:
                for e in ctx.message.attachments:
                    await user.send(file=(await e.to_file()))
                    await ctx.guild.get_channel(800708255194021918).send(file=(await e.to_file()))
        except discord.Forbidden:
            await ctx.send("Message couldn't be delivered.")

    @commands.Cog.listener()
    async def on_message_without_command(self, message):
        if message.guild is not None:
            return
        if message.author == self.bot.user:
            recipient = (await self.bot.fetch_channel(message.channel.id)).recipient
            msg = f"Sent PM to {recipient} (`{recipient.id if recipient else 'Unknown'}`)"
            if message.embeds:
                embed = discord.Embed.from_dict(
                    {**message.embeds[0].to_dict(), "timestamp": str(message.created_at)}
                )
                await self.bot.get_guild(749863506228150383).get_channel(800708255194021918).send(
                    msg, embed=embed
                )
        else:
            await self.bot.get_guild(749863506228150383).get_channel(800708255194021918).send(
                f"Incoming message from {message.author}({message.author.id}):\n{message.content}"
            )
            if message.attachments:
                for e in message.attachments:
                    await self.bot.get_guild(749863506228150383).get_channel(
                        800708255194021918
                    ).send(file=(await e.to_file()))
