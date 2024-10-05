from typing import Self

from graphene import Mutation, ID, Boolean  # type: ignore[import-untyped]
from dp.settings import REPOSITORIES
from dp.domain.person.service import edit_person
from dp.domain.person.dto import PersonDto
from dp.domain.person.gql.object_type import PersonInputObjectType  # type: ignore[import-untyped]


class EditPersonMutation(Mutation):
    class Arguments:
        person_id = ID()
        person_input = PersonInputObjectType(required=True)

    ok = Boolean()

    @classmethod
    def mutate(cls, root, info, person_id: str, person_input: PersonDto) -> Self:
        repository = REPOSITORIES["person_repository"]
        edit_person(repository, person_id, person_input)
        return cls(ok=True)
