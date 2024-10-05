from graphene import List, NonNull  # type: ignore[import-untyped]

from dp.domain.person.base_model import Person
from dp.domain.person.gql.object_type import PersonObjectType  # type: ignore[import-untyped]
from dp.domain.person.service import list_person
from dp.settings import REPOSITORIES


class PersonListQuery:
    person_list = List(NonNull(PersonObjectType), required=True)

    @staticmethod
    def resolve_person_list(root, info) -> list[Person]:
        repository = REPOSITORIES["person_repository"]
        return list_person(repository)
