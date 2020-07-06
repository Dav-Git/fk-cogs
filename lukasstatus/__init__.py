from .lukasstatus import LukasStatus


def setup(bot):
    bot.add_cog(LukasStatus(bot))
