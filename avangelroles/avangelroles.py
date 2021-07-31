from redbot.core import commands
import discord


class AvAngelRoles(commands.Cog):
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        await member.add_roles(member.guild.get_role(866475572250148864))

    @commands.Cog.listener()
    async def on_member_change(self, before, after):
        before_ids = [r.id for r in before.roles]
        after_ids = [r.id for r in after.roles]
        await before.guild.get_channel(870041008052772874).send(
            f"Before {before_ids}\nAfter {after_ids}."
        )
        if before_ids != after_ids:
            if 866476884253605888 in after_ids or 866491067045511228 in after_ids:
                if 866475572250148864 in before_ids:
                    await after.remove_roles(after.guild.get_role(866475572250148864))
            else:
                if 866475572250148864 not in before_ids:
                    await after.add_roles(after.guild.get_role(866475572250148864))
