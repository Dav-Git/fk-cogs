from .customblocklist import CustomBlockList

old_blocklist_add_command = None


async def setup(bot):
    global old_blocklist_add_command
    group = bot.get_command("blocklist")
    old_blocklist_add_command = group.get_command("add")
    group.remove_command("add")
    cog = CustomBlockList(bot)
    bot.add_cog(cog)
    await cog.initialize(bot)


def teardown(bot):
    if old_blocklist_add_command is None:
        return
    group = bot.get_command("blocklist")
    group.add_command(old_blocklist_add_command)