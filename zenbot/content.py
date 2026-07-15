import random

ENCOURAGEMENTS = (
    "You do not have to solve everything today. One small step is enough.",
    "Be proud of the effort nobody else can see.",
    "Rest is part of progress, not a reward you have to earn.",
    "A difficult day does not erase how far you have come.",
    "Start where you are, use what you have, and do what you can.",
    "You are allowed to take up space and ask for support.",
    "Keep going gently. Consistency does not have to look dramatic.",
    "Your pace is still a pace.",
)

QUOTES = (
    ("No act of kindness, no matter how small, is ever wasted.", "Aesop"),
    ("The best way out is always through.", "Robert Frost"),
    ("Nothing can bring you peace but yourself.", "Ralph Waldo Emerson"),
    ("It always seems impossible until it is done.", "Nelson Mandela"),
    ("Act as if what you do makes a difference. It does.", "William James"),
)

REFLECTION_PROMPTS = (
    "What gave you a little energy today?",
    "What is one thing you handled better than you would have a year ago?",
    "What can you let go of for the rest of today?",
    "Who made your day easier, and how could you thank them?",
    "What is one small thing you are looking forward to?",
    "If your closest friend felt this way, what would you tell them?",
    "What is within your control right now?",
    "Name one ordinary thing you are grateful for today.",
)


def encouragement() -> str:
    return random.choice(ENCOURAGEMENTS)


def quote() -> tuple[str, str]:
    return random.choice(QUOTES)


def reflection_prompt() -> str:
    return random.choice(REFLECTION_PROMPTS)
