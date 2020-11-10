from redbot.core import commands, Config


class JoinFlag(commands.Cog):
    async def red_delete_data_for_user(self, *, requester, user_id):
        pass

    def __init__(self):
        self.config = Config.get_conf(self, 12345, force_registration=True)
        self.config.register_member(flag=None)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 332834024831582210:
            if await self.config.member(member).flag():
                await member.guild.get_channel(449945421742211082).send(
                    f"**This member was flagged after leaving!**\n{await self.config.member(member).flag()}"
                )
                await self.config.member(member).flag.set(None)

    @commands.command()
    @commands.mod()
    async def joinflag(self, ctx, user_id: int, *, text: str):
        await self.config.member_from_ids(ctx.guild.id, user_id).flag.set(text)
