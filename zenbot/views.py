from __future__ import annotations

import discord


class CheckInView(discord.ui.View):
    def __init__(self, owner_id: int) -> None:
        super().__init__(timeout=120)
        self.owner_id = owner_id

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id == self.owner_id:
            return True
        await interaction.response.send_message(
            "This check-in belongs to someone else. Use `/checkin` for your own.",
            ephemeral=True,
        )
        return False

    async def _reply(self, interaction: discord.Interaction, message: str) -> None:
        for item in self.children:
            item.disabled = True
        await interaction.response.edit_message(content=message, embed=None, view=self)

    @discord.ui.button(label="Doing well", emoji="🌿", style=discord.ButtonStyle.success)
    async def well(self, interaction: discord.Interaction, _: discord.ui.Button) -> None:
        await self._reply(
            interaction,
            "Glad to hear it. What is one thing you want to carry into the rest of your day?",
        )

    @discord.ui.button(label="Getting by", emoji="☁️", style=discord.ButtonStyle.primary)
    async def okay(self, interaction: discord.Interaction, _: discord.ui.Button) -> None:
        await self._reply(
            interaction,
            "Getting by is enough. Pick one manageable thing, then give yourself room to breathe.",
        )

    @discord.ui.button(label="Having a hard time", emoji="💛", style=discord.ButtonStyle.secondary)
    async def struggling(self, interaction: discord.Interaction, _: discord.ui.Button) -> None:
        await self._reply(
            interaction,
            "I’m sorry today is heavy. Consider messaging someone you trust. "
            "If you may be in immediate danger, contact local emergency services now.",
        )
