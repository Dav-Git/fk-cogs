import discord
from redbot.core import commands, checks


class CustomDM(commands.Cog):
    async def red_delete_data_for_user(self, *, requester, user_id):
        pass  # This cog stores no EUD

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="message")
    @checks.admin()
    async def send_pm(self, ctx, user: discord.User, *, text: str):
        try:
            await user.send(text)
            await ctx.guild.get_channel(717915738739965952).send(
                f"Outbound message from {ctx.author.mention} to {user.name}#{user.discriminator}({user.id}):\n{text}"
            )
            if ctx.message.attachments:
                for e in ctx.message.attachments:
                    await user.send(file=(await e.to_file()))
                    await ctx.guild.get_channel(717915738739965952).send(file=(await e.to_file()))
        except discord.Forbidden:
            await ctx.send("Message couldn't be delivered.")

    @commands.Cog.listener()
    async def on_message_without_command(self, message):
        if message.guild is not None:
            return
        if message.author == self.bot.user:
            msg = f"Sent PM to {message.channel.recipient} (`{message.channel.recipient.id}`)"
            if message.embeds:
                embed = discord.Embed.from_dict(
                    {**message.embeds[0].to_dict(), "timestamp": str(message.created_at)}
                )
                await self.bot.get_guild(332834024831582210).get_channel(717915738739965952).send(
                    msg, embed=embed
                )
        else:
            await self.bot.get_guild(332834024831582210).get_channel(717915738739965952).send(
                f"Incoming message from {message.author.name}#{message.author.discriminator}({message.author.id}):\n{message.content}"
            )
            if message.attachments:
                for e in message.attachments:
                    await self.bot.get_guild(332834024831582210).get_channel(
                        717915738739965952
                    ).send(file=(await e.to_file()))
