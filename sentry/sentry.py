import logging
import sentry_sdk
from redbot.core import commands
from sentry_sdk.integrations.aiohttp import AioHttpIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk import add_breadcrumb


class Sentry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def initialize(self):
        self.connectSentry((await self.bot.get_shared_api_tokens("sentry")).get("dsn", ""))

    def cog_unload(self) -> None:
        self.closeSentry()

    def closeSentry(self):
        client = sentry_sdk.Hub.current.client
        if client is not None:
            client.close()

    def connectSentry(self, token):
        sentry_sdk.init(
            token,
            traces_sample_rate=1.0,
            shutdown_timeout=0.1,
            integrations=[
                AioHttpIntegration(),
                LoggingIntegration(level=logging.INFO, event_level=logging.ERROR),
            ],
        )

    @commands.admin()
    @commands.group()
    async def sentry(self, ctx):
        pass

    @sentry.command()
    async def test(self, ctx):
        1 / 0

    @commands.admin()
    @sentry.command(hidden=True)
    async def reinit(self, ctx):
        self.closeSentry()
        self.connectSentry((await self.bot.get_shared_api_tokens("sentry")).get("dsn", ""))
        await ctx.tick()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if not ctx.command:
            return
        add_breadcrumb(
            type="user",
            category="on_command_error",
            message=f'command "{ctx.command.name}" failed for {ctx.author.name} ({ctx.author.id})',
            level="error",
        )

    @commands.Cog.listener()
    async def on_command(self, ctx):
        add_breadcrumb(
            type="user",
            category="on_command",
            message=f'command "{ctx.command.name}" ran for {ctx.author.name} ({ctx.author.id})',
            level="info",
        )

    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        add_breadcrumb(
            type="user",
            category="on_command_completion",
            message=f'command "{ctx.command.name}" completed for {ctx.author.name} ({ctx.author.id})',
            level="info",
        )
