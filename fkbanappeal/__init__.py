from .fkbanappeal import FKBanAppeal

__red_end_user_data_statement__ = "This cog does not store end user data."

old_ban_command = None


async def setup(bot):
    global old_ban_command
    old_ban_command = bot.get_command("ban")
    bot.remove_command("ban")
    cog = FKBanAppeal(bot)
    await bot.add_cog(cog)


async def teardown(bot):
    if old_ban_command is None:
        return
    bot.add_command(old_ban_command)
