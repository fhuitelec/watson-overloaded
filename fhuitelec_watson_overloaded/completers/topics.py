# coding: utf-8

from typing import List

from prompt_toolkit.completion import FuzzyWordCompleter, Completer
from prompt_toolkit.validation import Validator, ValidationError

from fhuitelec_watson_overloaded.model.topic import Topic


def get_topic_completer_from_moods(topics: List[Topic]) -> Completer:
    return FuzzyWordCompleter(
        words=[topic.human_readable for topic in topics],
        meta_dict={topic.human_readable: topic.description for topic in topics},
    )


class TopicValidator(Validator):
    def __init__(self, topics: List[Topic]):
        self.acceptable_topic_ids = [topic.human_readable for topic in topics]

    def validate(self, document):
        text = document.text

        if text.strip() in self.acceptable_topic_ids:
            return

        raise ValidationError(message='Must be a valid topic')
