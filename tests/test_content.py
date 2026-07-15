from zenbot.content import (
    ENCOURAGEMENTS,
    QUOTES,
    REFLECTION_PROMPTS,
    encouragement,
    quote,
    reflection_prompt,
)


def test_random_content_comes_from_curated_collections() -> None:
    assert encouragement() in ENCOURAGEMENTS
    assert quote() in QUOTES
    assert reflection_prompt() in REFLECTION_PROMPTS


def test_curated_content_is_not_empty() -> None:
    assert all(ENCOURAGEMENTS)
    assert all(text and author for text, author in QUOTES)
    assert all(REFLECTION_PROMPTS)
