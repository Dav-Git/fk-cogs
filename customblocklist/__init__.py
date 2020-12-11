from .customblocklist import CustomBlockList

old_blocklist_commands = None


async def setup(bot):
    global old_blocklist_commands
    group = bot.get_command("blocklist")
    bot.remove_command(group)
    old_blocklist_commands = group
    cog = CustomBlockList(bot)
    bot.add_cog(cog)
    await cog.initialize(bot)


def teardown(bot):
    if old_blocklist_commands is None:
        return
    bot.add_command(old_blocklist_commands)