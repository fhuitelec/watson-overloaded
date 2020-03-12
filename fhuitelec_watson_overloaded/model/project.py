# coding: utf-8

from typing import List, Optional


class Project:
    def __init__(self, identifier: str, human_readable: str):
        self.identifier = identifier
        self.human_readable = human_readable


class ProjectConverter:
    @staticmethod
    def convert(raw_project) -> Project:
        return Project(
            raw_project['id'],
            raw_project['human_readable']
        )

    @classmethod
    def convert_all(cls, raw_projects: List[dict]) -> List[Project]:
        return [cls.convert(project) for project in raw_projects]


def get_project_from_human_readable(projects: List[Project], project: str) -> Optional[Project]:
    for existing_project in projects:
        if existing_project.human_readable == project:
            return existing_project

    return None
