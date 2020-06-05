import discord
from redbot.core import commands, checks


class CustomDM(commands.Cog):
    @commands.command(name="message")
    @checks.admin()
    async def send_pm(self, ctx, user: discord.User, *, text: str):
        try:
            await user.send(text)
            await ctx.guild.get_channel(717915738739965952).send(
                f"Outbound message from {ctx.author.mention} to {user.name}#{user.discriminator}:\n{text}"
            )
            if ctx.message.attachments:
                for e in ctx.message.attachments:
                    await user.send(file=(await e.to_file()))
                    await ctx.guild.get_channel(717915738739965952).send(file=(await e.to_file()))
        except discord.Forbidden:
            await ctx.send("Message couldn't be delivered.")
