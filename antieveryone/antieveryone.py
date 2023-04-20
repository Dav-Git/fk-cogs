from redbot.core import commands


class AntiEveryone(commands.Cog):
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 160527441520099328: # Don't block Rach. Oopsie
            return
        if not message.author.bot:
            if message.guild.id == 332834024831582210:
                if not message.guild.get_role(332834961407213568) in message.author.roles: #Admin Abooz
                    if "@everyone" in message.content:
                        await message.delete()
                        await message.channel.send(
                            "https://tenor.com/view/ping-discord-vr-chat-everyone-gif-16977940"
                        )
                        await message.channel.send(f"Good job {message.author.mention}...")
                        await message.guild.get_channel(449944250507984896).send(
                            "https://tenor.com/view/ping-discord-vr-chat-everyone-gif-16977940"
                        )
                        await message.guild.get_channel(449944250507984896).send(
                            f"{message.author}({message.author.id}) just tried to @everyone in {message.channel.mention}. This is the message they attempted to send:\n``{message.content}``"
                        )