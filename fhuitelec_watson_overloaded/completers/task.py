# coding: utf-8

from typing import List

from prompt_toolkit.completion import FuzzyWordCompleter, Completer
from prompt_toolkit.validation import Validator, ValidationError

from fhuitelec_watson_overloaded.model.project import Project


class TaskValidator(Validator):
    def validate(self, document):
        text = document.text

        if text.strip() != '':
            return

        raise ValidationError(message='Task must not be empty')
