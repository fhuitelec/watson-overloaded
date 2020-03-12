# coding: utf-8

from typing import Optional, List

from fhuitelec_watson_overloaded.model.mood import Mood, get_mood_from_identifier
from fhuitelec_watson_overloaded.model.project import Project, get_project_from_human_readable
from fhuitelec_watson_overloaded.model.topic import Topic, get_topic_from_human_readable


class Choice:
    task: Optional[str]
    topic: Optional[Topic]
    mood: Optional[Mood]

    def __init__(self, topics: List[Topic], projects: List[Project], moods: List[Mood]):
        self.topics = topics
        self.projects = projects
        self.moods = moods
        self.topic = None
        self.project = None
        self.task = None
        self.mood = None

    def add_topic(self, raw_topic):
        self.topic = get_topic_from_human_readable(self.topics, raw_topic)

    def add_project(self, raw_project):
        self.project = get_project_from_human_readable(self.projects, raw_project)

    def add_task(self, task):
        self.task = task

    def add_mood(self, raw_mood):
        self.mood = get_mood_from_identifier(self.moods, raw_mood)

    def is_choice_complete(self) -> bool:
        return self.task is not None \
            and self.topic is not None
