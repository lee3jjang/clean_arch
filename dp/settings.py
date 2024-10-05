from typing import TypedDict

from dp.domain.person.repository import PersonRepository


class Repositories(TypedDict, total=False):
    person_repository: PersonRepository


REPOSITORIES: Repositories = {}
