from graphene import Field, ID  # type: ignore[import-untyped]

from dp.domain.person.base_model import Person
from dp.domain.person.gql.object_type import PersonObjectType  # type: ignore[import-untyped]
from dp.domain.person.service import get_person
from dp.settings import REPOSITORIES


class PersonQuery:
    person = Field(PersonObjectType, required=True, person_id=ID())

    @staticmethod
    def resolve_person(root, info, person_id: str) -> Person:
        repository = REPOSITORIES["person_repository"]
        return get_person(repository, person_id)
