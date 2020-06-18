from .claw import Claw


async def setup(bot):
    cog = Claw()
    await cog.initialize()
    bot.add_cog(cog)
