# Zen Bot 🌿

A calm Discord companion for healthier online communities, built around small
moments of encouragement, reflection, and care.

## The story behind Zen Bot

I originally made Zen Bot when I was 12 and published the first version in
2022. It was one of my early coding projects: a single Python file running a
Discord bot on Replit. The original bot greeted members, shared motivational
quotes, sent random encouragement and emojis, displayed server rules, and
provided a few basic moderation commands.

Years later, I returned to the project to see what I could make with everything
I had learned since then. Rather than hiding the old project, this repository
keeps its history and turns it into the foundation for something more focused.

Zen Bot 2.0 keeps the warmth and simplicity of the original idea, but gives it
a clearer purpose: helping online communities slow down, check in, and support
one another. The code has also been rebuilt with modern Discord slash commands,
a modular structure, safer configuration, tests, and improved moderation.

## Then and now

| Original Zen Bot | Zen Bot 2.0 |
| --- | --- |
| Prefix commands such as `^cheer` | Discoverable Discord slash commands |
| External quote request | Reliable curated quotes and encouragement |
| One large Python file | Maintainable commands split into extensions |
| Public text responses | Private check-ins and reflection tools |
| Replit Flask keep-alive workaround | Hosting-independent bot process |
| Basic kick and ban commands | Permission-checked moderation tools |

The goal is not to erase what I made at 12. It is to show how an early project
can grow alongside its creator.

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

Never commit your bot token. If a token is ever pasted into a chat, screenshot,
or public file, reset it immediately in the Discord Developer Portal.

## Project structure

```text
main.py                  Entry point
zenbot/bot.py            Bot startup and command synchronization
zenbot/cogs/wellbeing.py Wellbeing slash commands
zenbot/cogs/community.py Community and moderation commands
zenbot/content.py        Curated prompts, quotes, and encouragement
zenbot/views.py          Interactive Discord components
tests/                   Automated checks
```

## Status

Zen Bot 2.0 is an active revival of the original project. The current version
is intentionally small and focused so each new feature supports its wellbeing
or community purpose.
