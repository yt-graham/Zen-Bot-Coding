# Zen Bot 🌿

A calm Discord companion for healthier online communities. Zen Bot began as a
fun project when I was 12 and has been reimagined with modern slash commands,
private mood check-ins, breathing exercises, encouragement, and lightweight
moderation.

## Commands

- `/zen` — learn what the bot can do
- `/checkin` — private interactive mood check-in
- `/breathe` — guided 4-4-6 breathing exercise
- `/cheer` — receive some encouragement
- `/inspire` — read an inspiring quote
- `/ground` — private 5-4-3-2-1 grounding exercise
- `/reflect` — receive a private journaling prompt
- `/timeout` — temporarily restrict a member
- `/clear` — remove up to 100 recent messages
- `/kick` and `/ban` — permission-protected moderation

## Run locally

1. Install Python 3.9+ and [Poetry](https://python-poetry.org/).
2. Create a Discord application and bot in the Developer Portal.
3. Invite it with the `bot` and `applications.commands` scopes.
4. Copy `.env.example` to `.env` and add your token.
5. Install and start:

   ```bash
   poetry install
   poetry run python main.py
   ```

Set `DEV_GUILD_ID` while developing so command changes appear immediately in
one test server. Without it, global Discord command updates can take longer.

Never commit your bot token. If the original token was ever published, reset it
in the Discord Developer Portal before running this version.
