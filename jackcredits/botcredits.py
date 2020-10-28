from redbot.core import commands
from redbot.core.utils.chat_formatting import pagify
import discord


class BotCredits(commands.Cog):
    async def red_delete_data_for_user(self, *, requester, user_id):
        pass  # This cog stores no EUD

    def __init__(self, bot):
        self.bot = bot
        # black

    @commands.command()
    async def credits(self, ctx):
        """Credits for everyone who makes this bot possible."""
        repo_cog = self.bot.get_cog("Downloader")
        embed = discord.Embed(
            title=f"{self.bot.user.name}'s Credits",
            description=f"Credits for all people and services that help make {self.bot.user.name} work.",
            timestamp=self.bot.user.created_at,
        )
        embed.set_footer(text=f"{self.bot.user.name} exists since")
        # discord.py, where is my icon_url_as?
        embed.set_thumbnail(
            url="https://media.discordapp.net/attachments/765366487438983208/768899405872365598/Defender_Bot_-_white_border.png?width=461&height=461"
        )
        embed.add_field(
            name="Red-DiscordBot",
            value=f"{self.bot.user.name} is an instance of [Red bot](https://github.com/Cog-Creators/Red-DiscordBot), "
            "created by [Twentysix](https://github.com/Twentysix26), and maintained by an"
            "[awesome community](https://github.com/Cog-Creators/Red-DiscordBot/graphs/contributors).",
            inline=False,
        )
        embed.add_field(
            name="Hosting",
            value="This instance is maintained by Dav#6998.",
            inline=False,
        )
        used_repos = {c.repo_name for c in await repo_cog.installed_cogs()}
        cogs_credits = (
            f"*Use `{ctx.clean_prefix}findcog <command>` to find out who authored a specific command.*\n"
            + "\n".join(
                sorted(
                    (
                        f"**[{repo.url.split('/')[4]}]({repo.url})**: {', '.join(repo.author) or repo.url.split('/')[3]}"
                        for repo in repo_cog._repo_manager.repos
                        if repo.url.startswith("http") and repo.name in used_repos
                    ),
                    key=lambda k: k.title(),
                )
            )
        )
        cogs_credits = list(pagify(cogs_credits, page_length=1024))
        embed.add_field(
            name="Third-party modules (Cogs) and their creators",
            value=cogs_credits[0],
            inline=False,
        )
        cogs_credits.pop(0)
        for page in cogs_credits:
            embed.add_field(name="\N{Zero Width Space}", value=page, inline=False)
        await ctx.send(embed=embed)
