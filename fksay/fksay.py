from redbot.core import commands
import discord


class FkSay(commands.Cog):
    @commands.mod()
    @commands.command()
    async def say(self, ctx, channel: discord.TextChannel, *, message: str):
        files = []
        files2 = []
        if ctx.message.attachments:
            for attachment in ctx.message.attachments:
                files.append(await attachment.to_file())
        message = await channel.send(
            message, files=files, allowed_mentions=discord.AllowedMentions.all()
        )
        await ctx.send(
            f"{ctx.author.mention} ({ctx.author.display_name}) made me talk in {channel.mention}:\n{message.jump_url}"
        )
        await ctx.tick()
