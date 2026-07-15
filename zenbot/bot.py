from __future__ import annotations

import logging

import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

from zenbot.config import Config

EXTENSIONS = ("zenbot.cogs.wellbeing", "zenbot.cogs.community")


class ZenBot(commands.Bot):
    def __init__(self, config: Config) -> None:
        super().__init__(command_prefix=commands.when_mentioned, intents=discord.Intents.default())
        self.config = config

    async def setup_hook(self) -> None:
        for extension in EXTENSIONS:
            await self.load_extension(extension)

        if self.config.dev_guild_id:
            guild = discord.Object(id=self.config.dev_guild_id)
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
            logging.info("Synced commands to development guild %s", guild.id)
        else:
            await self.tree.sync()
            logging.info("Synced global commands")

    async def on_ready(self) -> None:
        await self.change_presence(activity=discord.CustomActivity(name="Take a breath 🌿"))
        logging.info("Ready as %s (%s)", self.user, self.user.id if self.user else "unknown")


async def on_tree_error(
    interaction: discord.Interaction, error: app_commands.AppCommandError
) -> None:
    if isinstance(error, app_commands.MissingPermissions):
        message = "You do not have permission to use that command."
    elif isinstance(error, app_commands.BotMissingPermissions):
        message = "I do not have the server permissions needed to do that."
    else:
        logging.exception("Unhandled command error", exc_info=error)
        message = "Something went wrong. Please try again in a moment."

    if interaction.response.is_done():
        await interaction.followup.send(message, ephemeral=True)
    else:
        await interaction.response.send_message(message, ephemeral=True)


def run() -> None:
    load_dotenv()
    config = Config.from_env()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
    bot = ZenBot(config)
    bot.tree.on_error = on_tree_error
    bot.run(config.token, log_handler=None)
