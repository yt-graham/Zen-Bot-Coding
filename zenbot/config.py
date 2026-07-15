from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    token: str
    dev_guild_id: int | None = None

    @classmethod
    def from_env(cls) -> Config:
        token = os.getenv("DISCORD_TOKEN", "").strip()
        if not token:
            raise RuntimeError(
                "DISCORD_TOKEN is missing. Copy .env.example to .env and add your bot token."
            )

        guild_value = os.getenv("DEV_GUILD_ID", "").strip()
        try:
            guild_id = int(guild_value) if guild_value else None
        except ValueError as exc:
            raise RuntimeError("DEV_GUILD_ID must be a Discord server ID.") from exc

        return cls(token=token, dev_guild_id=guild_id)
