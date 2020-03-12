# coding: utf-8
from fhuitelec_watson_overloaded.cli.choice import Choice


def generate_command_from_choice(choice: Choice):
    if not choice.is_choice_complete():
        raise ValueError('Choice must be valid')

    project = ''
    if choice.project is not None:
        project = '"{}"'.format(choice.project.identifier)

    mood = ''
    if choice.mood is not None:
        mood = '"{}"'.format(choice.mood.identifier)

    return '"{task}" "+{topic}" {project} {mood}'.format(
        task=choice.task,
        topic=choice.topic.identifier,
        project=project,
        mood=mood
    ).strip()
