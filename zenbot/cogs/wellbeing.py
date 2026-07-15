from __future__ import annotations

import asyncio

import discord
from discord import app_commands
from discord.ext import commands

from zenbot.content import encouragement, quote, reflection_prompt
from zenbot.views import CheckInView

GREEN = discord.Color.from_rgb(78, 168, 126)


class Wellbeing(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(description="Receive a little encouragement")
    async def cheer(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(f"💚 {encouragement()}")

    @app_commands.command(description="Read an inspiring quote")
    async def inspire(self, interaction: discord.Interaction) -> None:
        text, author = quote()
        embed = discord.Embed(description=f"“{text}”", color=GREEN)
        embed.set_footer(text=f"— {author}")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(description="Pause for a guided breathing exercise")
    async def breathe(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("🌬️ **Breathe in…** 4 seconds", ephemeral=True)
        await asyncio.sleep(4)
        await interaction.edit_original_response(content="⏸️ **Hold…** 4 seconds")
        await asyncio.sleep(4)
        await interaction.edit_original_response(content="🍃 **Breathe out…** 6 seconds")
        await asyncio.sleep(6)
        await interaction.edit_original_response(
            content="✨ Done. Notice how you feel before moving on."
        )

    @app_commands.command(description="Take a private moment to check in with yourself")
    async def checkin(self, interaction: discord.Interaction) -> None:
        embed = discord.Embed(
            title="How are you feeling right now?",
            description="There is no wrong answer. Choose the closest option.",
            color=GREEN,
        )
        await interaction.response.send_message(
            embed=embed, view=CheckInView(interaction.user.id), ephemeral=True
        )

    @app_commands.command(description="Use the 5-4-3-2-1 grounding technique")
    async def ground(self, interaction: discord.Interaction) -> None:
        embed = discord.Embed(
            title="5-4-3-2-1 grounding",
            description="Slow down and notice your surroundings. There is no need to rush.",
            color=GREEN,
        )
        embed.add_field(
            name="5 things you can see", value="Let your eyes settle on each one.", inline=False
        )
        embed.add_field(
            name="4 things you can feel",
            value="Notice texture, temperature, or pressure.",
            inline=False,
        )
        embed.add_field(
            name="3 things you can hear", value="Listen for sounds near and far.", inline=False
        )
        embed.add_field(
            name="2 things you can smell", value="Or think of two scents you enjoy.", inline=False
        )
        embed.add_field(
            name="1 thing you can taste",
            value="Take one slow breath when you finish.",
            inline=False,
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(description="Receive a private prompt for reflection")
    async def reflect(self, interaction: discord.Interaction) -> None:
        embed = discord.Embed(
            title="A moment to reflect",
            description=reflection_prompt(),
            color=GREEN,
        )
        embed.set_footer(
            text="You can write your answer somewhere private—or simply think about it."
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Wellbeing(bot))
