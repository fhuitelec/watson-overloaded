# coding: utf-8

from typing import List, Optional


class Topic:
    def __init__(self, identifier: str, human_readable: str, description: str, human_readable_aliases: List[str]):
        self.identifier = identifier
        self.human_readable = human_readable
        self.description = description
        self.human_readable_aliases = human_readable_aliases


class TopicConverter:
    @staticmethod
    def convert(raw_topic) -> Topic:
        return Topic(
            raw_topic['id'],
            raw_topic['human_readable'],
            raw_topic['description'],
            raw_topic['human_readable_aliases'] if 'human_readable_aliases' in raw_topic else [],
        )

    @classmethod
    def convert_all(cls, raw_topics: List[dict]) -> List[Topic]:
        return [cls.convert(topic) for topic in raw_topics]


def get_topic_from_human_readable(topics: List[Topic], topic: str) -> Optional[Topic]:
    for existing_topic in topics:
        if existing_topic.human_readable == topic:
            return existing_topic

    return None
