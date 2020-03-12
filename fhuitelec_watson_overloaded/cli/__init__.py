from typing import Optional

from fhuitelec_watson_overloaded.model.mood import Mood
from fhuitelec_watson_overloaded.model.topic import Topic


class Choice:
    task: Optional[str]
    topic: Optional[Topic]
    mood: Optional[Mood]

    def __init__(self):
        self.task = None
        self.topic = None
        self.mood = None

