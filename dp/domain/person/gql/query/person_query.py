from graphene import Field, ID  # type: ignore[import-untyped]

from dp.domain.person.model import Person
from dp.domain.person.gql.object_type import PersonObjectType  # type: ignore[import-untyped]
from dp.domain.person.service import get_person
from dp.repository import REPOSITORY


class PersonQuery:
    person = Field(PersonObjectType, required=True, person_id=ID())

    @staticmethod
    def resolve_person(root, info, person_id: str) -> Person:
        repository = REPOSITORY["person"]
        return get_person(repository, person_id)
