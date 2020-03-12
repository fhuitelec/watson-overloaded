# coding: utf-8

from prompt_toolkit import HTML

from fhuitelec_watson_overloaded.cli.choice import Choice


class Toolbar:
    def __init__(self):
        self.topic = None
        self.project = None
        self.task = None
        self.mood = None

    def bottom_toolbar(self):
        topic = self.topic
        if topic is None:
            topic = '<style bg="darkred">N/A</style>'
        project = self.project
        if project is None:
            project = '<style bg="darkred">N/A</style>'
        task = self.task
        if task is None:
            task = '<style bg="darkred">N/A</style>'
        mood = self.mood
        if mood is None:
            mood = '<style bg="darkred">N/A</style>'

        return HTML(
            '<b>Topic:</b> {topic} | <b>Project:</b> {project} | <b>Task:</b> {task} | <b>Mood:</b> {mood}'.format(
                topic=topic, project=project, task=task, mood=mood,
            )
        )

    def register_choice(self, choice: Choice):
        self.project = choice.project.human_readable if choice.project is not None else None
        self.topic = choice.topic.human_readable if choice.topic is not None else None
        self.task = choice.task
        self.mood = choice.mood.emoji if choice.mood is not None else None
