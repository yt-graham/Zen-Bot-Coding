from __future__ import annotations

from datetime import timedelta

import discord
from discord import app_commands
from discord.ext import commands

GREEN = discord.Color.from_rgb(78, 168, 126)


class Community(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(description="Learn what Zen Bot can do")
    async def zen(self, interaction: discord.Interaction) -> None:
        embed = discord.Embed(
            title="Zen Bot",
            description="A calm companion for healthier online communities.",
            color=GREEN,
        )
        embed.add_field(
            name="Wellbeing", value="`/checkin`  `/breathe`  `/cheer`  `/inspire`", inline=False
        )
        embed.add_field(name="Reset", value="`/ground`  `/reflect`", inline=False)
        embed.add_field(
            name="Community", value="`/timeout`  `/clear`  `/kick`  `/ban`", inline=False
        )
        embed.set_footer(text="Originally built by Jamie at age 12 • Reimagined with care")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(description="Remove a member from this server")
    @app_commands.describe(member="Member to remove", reason="Reason shown in the audit log")
    @app_commands.checks.has_permissions(kick_members=True)
    @app_commands.checks.bot_has_permissions(kick_members=True)
    async def kick(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        reason: str = "No reason provided",
    ) -> None:
        await member.kick(reason=f"{reason} — requested by {interaction.user}")
        await interaction.response.send_message(f"👋 {member.mention} was kicked. Reason: {reason}")

    @app_commands.command(description="Ban a member from this server")
    @app_commands.describe(member="Member to ban", reason="Reason shown in the audit log")
    @app_commands.checks.has_permissions(ban_members=True)
    @app_commands.checks.bot_has_permissions(ban_members=True)
    async def ban(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        reason: str = "No reason provided",
    ) -> None:
        await member.ban(reason=f"{reason} — requested by {interaction.user}")
        await interaction.response.send_message(f"🔨 {member.mention} was banned. Reason: {reason}")

    @app_commands.command(description="Temporarily prevent a member from participating")
    @app_commands.describe(
        member="Member to time out",
        minutes="Duration from 1 minute to 1 week",
        reason="Reason shown in the audit log",
    )
    @app_commands.checks.has_permissions(moderate_members=True)
    @app_commands.checks.bot_has_permissions(moderate_members=True)
    async def timeout(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        minutes: app_commands.Range[int, 1, 10080],
        reason: str = "No reason provided",
    ) -> None:
        if member.id == interaction.user.id:
            await interaction.response.send_message("You cannot time yourself out.", ephemeral=True)
            return
        await member.timeout(
            timedelta(minutes=minutes),
            reason=f"{reason} — requested by {interaction.user}",
        )
        await interaction.response.send_message(
            f"⏳ {member.mention} was timed out for {minutes} minute(s). Reason: {reason}"
        )

    @app_commands.command(description="Remove recent messages from this channel")
    @app_commands.describe(amount="Number of messages to remove, from 1 to 100")
    @app_commands.checks.has_permissions(manage_messages=True)
    @app_commands.checks.bot_has_permissions(manage_messages=True)
    async def clear(
        self, interaction: discord.Interaction, amount: app_commands.Range[int, 1, 100]
    ) -> None:
        channel = interaction.channel
        if not isinstance(channel, (discord.TextChannel, discord.Thread)):
            await interaction.response.send_message(
                "This command only works in server text channels.", ephemeral=True
            )
            return
        await interaction.response.defer(ephemeral=True)
        deleted = await channel.purge(limit=amount)
        await interaction.followup.send(f"🧹 Removed {len(deleted)} message(s).", ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Community(bot))
