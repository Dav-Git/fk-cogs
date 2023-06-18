from .customblocklist import CustomBlockList

__red_end_user_data_statement__ = "This cog does not store end user data. It logs user IDs added to the bot blocklist in a modlog entry."

old_blocklist_commands = None


async def setup(bot):
    global old_blocklist_commands
    group = bot.get_command("blocklist")
    bot.remove_command("blocklist")
    old_blocklist_commands = group
    cog = CustomBlockList(bot)
    await bot.add_cog(cog)
    await cog.initialize(bot)


async def teardown(bot):
    if old_blocklist_commands is None:
        return
    bot.add_command(old_blocklist_commands)
