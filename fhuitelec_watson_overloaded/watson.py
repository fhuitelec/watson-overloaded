# coding: utf-8

import sys
from os import getenv, makedirs
from os.path import join, expanduser, exists

from prompt_toolkit import prompt
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.history import FileHistory

from fhuitelec_watson_overloaded.cli.choice import Choice
from fhuitelec_watson_overloaded.cli.command_generator import generate_command_from_choice
from fhuitelec_watson_overloaded.cli.toolbar import Toolbar
from fhuitelec_watson_overloaded.completers.moods import MoodValidator, get_mood_completer_from_moods
from fhuitelec_watson_overloaded.completers.project import get_project_completer_from_moods, ProjectValidator
from fhuitelec_watson_overloaded.completers.task import TaskValidator
from fhuitelec_watson_overloaded.completers.topics import TopicValidator, get_topic_completer_from_moods
from fhuitelec_watson_overloaded.config import moods, topics, projects
from fhuitelec_watson_overloaded.model.mood import MoodConverter
from fhuitelec_watson_overloaded.model.project import ProjectConverter
from fhuitelec_watson_overloaded.model.topic import TopicConverter

moods = MoodConverter.convert_all(moods)
topics = TopicConverter.convert_all(topics)
projects = ProjectConverter.convert_all(projects)

toolbar = Toolbar()
choice = Choice(topics, projects, moods)

# Todo: key bindings pour changer de prompt (eg. Ctrl+M reprend le prompt "Mood")

# TODO: move elsewhere
data_folder = getenv(
    'XDG_DATA_HOME',
    join(
        expanduser('~'),
        '.local',
        'share'
    )
)

root_data_folder = join(
    data_folder,
    'watson-overloaded'
)

if not exists(root_data_folder):
    makedirs(root_data_folder)


def __main__():
    while not choice.is_choice_complete():
        try:
            user_topic = prompt(
                'Topic: ',
                history=FileHistory(join(root_data_folder, 'topics-history.txt')),
                auto_suggest=AutoSuggestFromHistory(),
                completer=get_topic_completer_from_moods(topics),
                validator=TopicValidator(topics),
                validate_while_typing=False,
                bottom_toolbar=toolbar.bottom_toolbar
            )
            choice.add_topic(user_topic)
            toolbar.register_choice(choice)

            project_topic = prompt(
                'Project: ',
                history=FileHistory(join(root_data_folder, 'projects-history.txt')),
                auto_suggest=AutoSuggestFromHistory(),
                completer=get_project_completer_from_moods(projects),
                validator=ProjectValidator(projects),
                validate_while_typing=False,
                bottom_toolbar=toolbar.bottom_toolbar
            )
            choice.add_project(project_topic)
            toolbar.register_choice(choice)

            user_task = prompt(
                'Task: ',
                history=FileHistory(join(root_data_folder, 'tasks-history.txt')),
                auto_suggest=AutoSuggestFromHistory(),
                validator=TaskValidator(),
                bottom_toolbar=toolbar.bottom_toolbar
            )
            choice.add_task(user_task)
            toolbar.register_choice(choice)

            user_mood = prompt(
                'Mood: ',
                completer=get_mood_completer_from_moods(moods),
                validator=MoodValidator(moods),
                validate_while_typing=False,
                bottom_toolbar=toolbar.bottom_toolbar
            )
            choice.add_mood(user_mood)
            toolbar.register_choice(choice)
        except KeyboardInterrupt:
            continue  # Control-C pressed. Try again.
        except EOFError:
            break  # Control-D pressed.

    if not choice.is_choice_complete():
        print('Input is incomplete, good bye!')
        sys.exit(1)

    print(
        generate_command_from_choice(choice)
    )
