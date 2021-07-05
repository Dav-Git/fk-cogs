from redbot.core import commands
import discord
from dislash import SlashClient, ActionRow, Button, ButtonStyle


class Pronouns(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.slash = SlashClient(bot)

    @commands.command()
    async def pronouns(self, ctx):
        button_row = ActionRow(
            Button(style=ButtonStyle.blurple, label="THEY/THEM", custom_id="they"),
            Button(style=ButtonStyle.blurple, label="SHE/HER", custom_id="she"),
            Button(style=ButtonStyle.blurple, label="HE/HIM", custom_id="he"),
            Button(style=ButtonStyle.grey, label="Ask me", custom_id="ask"),
            Button(style=ButtonStyle.red, label="Clear", custom_id="clear"),
        )
        msg = await ctx.send("Choose your preferred pronouns:", components=[button_row])
        on_click = msg.create_click_listener(timeout=120)

        @on_click.not_from_user(ctx.author, cancel_others=True, reset_timeout=False)
        async def on_wrong_user(inter):
            # Reply with a hidden message
            await inter.reply("You're not the author", ephemeral=True)

        @on_click.matching_id("he")
        async def on_test_button(inter):
            await inter.author.edit(nick=f"[HE/HIM]{ctx.author.display_name}")
            await self.changerole(inter.author, 860282987416387635)
            await inter.reply(
                "You've chosen the pronouns HE/HIM.\nFeel free to remove the prefix in your nickname if you don't like it."
            )

        @on_click.matching_id("she")
        async def on_test_button(inter):
            await inter.author.edit(nick=f"[SHE/HER]{ctx.author.display_name}")
            await self.changerole(inter.author, 860283063304192041)
            await inter.reply(
                "You've chosen the pronouns SHE/HER.\nFeel free to remove the prefix in your nickname if you don't like it."
            )

        @on_click.matching_id("they")
        async def on_test_button(inter):
            await inter.author.edit(nick=f"[THEY/THEM]{ctx.author.display_name}")
            await self.changerole(inter.author, 860283134595432450)
            await inter.reply(
                "You've chosen the pronouns THEY/THEM.\nFeel free to remove the prefix in your nickname if you don't like it."
            )

        @on_click.matching_id("ask")
        async def on_test_button(inter):
            await self.changerole(inter.author, 860283159639490611)
            await inter.reply("You've chosen to ask our members to ask you about your pronouns.")

        @on_click.matching_id("clear")
        async def on_test_button(inter):
            await self.changerole(inter.author, 00000000000000)
            await inter.reply("We have removed your pronoun role.")

        @on_click.timeout
        async def on_timeout():
            await msg.edit(content="Set your preferred pronouns with `-pronoun`.", components=[])

    @commands.group()
    async def setpronouns(self, ctx):
        """Set your pronouns"""
        pass

    @setpronouns.command()
    async def hehim(self, ctx):
        """Set your pronouns to he/him.\nYou may remove the prefix in your username if you don't want it."""
        await ctx.author.edit(nick=f"[HE/HIM]{ctx.author.display_name}")
        await self.changerole(ctx.author, 860282987416387635)
        await ctx.tick()

    @setpronouns.command()
    async def sheher(self, ctx):
        """Set your pronouns to she/her.\nYou may remove the prefix in your username if you don't want it."""
        await ctx.author.edit(nick=f"[SHE/HER]{ctx.author.display_name}")
        await self.changerole(ctx.author, 860283063304192041)
        await ctx.tick()

    @setpronouns.command()
    async def theythem(self, ctx):
        """Set your pronouns to they/them.\nYou may remove the prefix in your username if you don't want it."""
        await ctx.author.edit(nick=f"[THEY/THEM]{ctx.author.display_name}")
        await self.changerole(ctx.author, 860283134595432450)
        await ctx.tick()

    @setpronouns.command()
    async def custom(self, ctx, *, pronouns):
        """Set your pronouns to something we didn't offer as a default.\nWe recommend following the PRONOUN/POSSESSIVE format\nYou may remove the prefix in your username if you don't want it."""
        await ctx.author.edit(nick=f"[{pronouns}]{ctx.author.display_name}")
        await self.changerole(ctx.author, 860283159639490611)
        await ctx.tick()

    @setpronouns.command()
    async def clear(self, ctx):
        await self.changerole(ctx.author, 000000000000000000)
        await ctx.tick()

    async def changerole(self, member: discord.member, roleid: int) -> None:
        memberroleids = [r.id for r in member.roles]
        pronounroleids = [
            860282987416387635,
            860283063304192041,
            860283134595432450,
            860283159639490611,
        ]
        if roleid in memberroleids:
            return
        else:
            for rid in pronounroleids:
                if rid in memberroleids:
                    await member.remove_roles(member.guild.get_role(rid))
            try:
                await member.add_roles(member.guild.get_role(roleid))
            except discord.DiscordException:
                pass