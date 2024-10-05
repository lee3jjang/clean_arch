from typing import TypedDict

from dp.domain.person.repository.protocol import PersonRepositoryProtocol


class Repository(TypedDict, total=False):
    person: PersonRepositoryProtocol


REPOSITORY: Repository = {}
