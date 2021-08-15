from redbot.core import commands
import discord


class AvAngelRoles(commands.Cog):
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        await member.add_roles(member.guild.get_role(866475572250148864))

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        cool_roles = [
            876557447748263976,
            866475525554962472,
            866473144906022912,
            866491067045511228,
            869315211180519496,
        ]
        before_ids = [r.id for r in before.roles]
        after_ids = [r.id for r in after.roles]
        if before_ids != after_ids:
            if any(cool_role in after_ids for cool_role in cool_roles):
                if 866475572250148864 in before_ids:
                    await after.remove_roles(after.guild.get_role(866475572250148864))
            else:
                if 866475572250148864 not in before_ids:
                    await after.add_roles(after.guild.get_role(866475572250148864))
