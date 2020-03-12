# coding: utf-8

from typing import List, Optional


class Mood:
    def __init__(self, identifier: str, emoji: str):
        self.identifier = identifier
        self.emoji = emoji


class MoodConverter:
    @staticmethod
    def convert(raw_mood) -> Mood:
        return Mood(
            raw_mood['id'],
            raw_mood['emoji'],
        )

    @classmethod
    def convert_all(cls, raw_moods: List[dict]) -> List[Mood]:
        return [cls.convert(mood) for mood in raw_moods]


def get_mood_from_identifier(moods: List[Mood], mood_id: str) -> Optional[Mood]:
    for existing_mood in moods:
        if existing_mood.identifier == mood_id:
            return existing_mood

    return None
