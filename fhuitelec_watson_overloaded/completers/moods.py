# coding: utf-8

from typing import List

from prompt_toolkit.completion import WordCompleter, Completer
from prompt_toolkit.validation import Validator, ValidationError

from fhuitelec_watson_overloaded.model.mood import Mood


def get_mood_completer_from_moods(moods: List[Mood]) -> Completer:
    return WordCompleter(
        words=[mood.identifier for mood in moods],
        meta_dict={mood.identifier: mood.emoji for mood in moods},
        ignore_case=False,
        match_middle=True
    )


class MoodValidator(Validator):
    def __init__(self, moods: List[Mood]):
        self.acceptable_mood_ids = [mood.identifier for mood in moods]

    def validate(self, document):
        text = document.text

        if text.strip() == '':
            return

        if text.strip() in self.acceptable_mood_ids:
            return

        raise ValidationError(message='Must be a valid mood')
