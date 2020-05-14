import discord
from redbot.core import commands


class NoMic(commands.cog):
    """#No-mic manager"""

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        # Show #no-mic if member in VC
        if after.channel:
            if after.channel.id in [
                332834234135740416,
                518130862492090415,
                481820769568161793,
                706267818211147842,
            ]:
                overwrite = discord.PermissionOverwrite()
                overwrite.send_messages = True
                overwrite.read_messages = True
                await member.guild.get_channel(702969795389292584).set_permissions(
                    member, overwrite=overwrite
                )
            else:
                await member.guild.get_channel(702969795389292584).set_permissions(
                    member, overwrite=None
                )
        else:
            await member.guild.get_channel(702969795389292584).set_permissions(
                member, overwrite=None
            )
