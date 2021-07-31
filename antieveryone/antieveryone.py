from redbot.core import commands


class AntiEveryone(commands.Cog):
    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            if not message.guild.get_role(343116359724433429) in message.author.roles:
                if "@everyone" in message.content:
                    await message.delete()

            if message.guild.id == 343116121760595971:
                await message.guild.get_channel(820654163784106034).send(f"``{message.content}``")