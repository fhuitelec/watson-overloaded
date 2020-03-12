# coding: utf-8

from typing import List

from prompt_toolkit.completion import FuzzyWordCompleter, Completer
from prompt_toolkit.validation import Validator, ValidationError

from fhuitelec_watson_overloaded.model.project import Project


def get_project_completer_from_moods(projects: List[Project]) -> Completer:
    return FuzzyWordCompleter(
        words=[project.human_readable for project in projects]
    )


class ProjectValidator(Validator):
    def __init__(self, projects: List[Project]):
        self.acceptable_project_ids = [project.human_readable for project in projects]

    def validate(self, document):
        text = document.text

        if text.strip() == '':
            return

        if text.strip() in self.acceptable_project_ids:
            return

        raise ValidationError(message='Must be a valid project')
