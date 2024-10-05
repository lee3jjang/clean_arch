from typing import Self

from graphene import Mutation, ID, Field, Boolean  # type: ignore[import-untyped]
from dp.repository import REPOSITORY
from dp.domain.person.service import create_person
from dp.domain.person.dto import PersonDto
from dp.domain.person.gql.object_type import PersonInputObjectType  # type: ignore[import-untyped]


class CreatePersonMutation(Mutation):
    class Arguments:
        person_input = PersonInputObjectType(required=True)

    ok = Boolean()
    person_id = Field(ID)

    @classmethod
    def mutate(cls, root, info, person_input: PersonDto) -> Self:
        repository = REPOSITORY["person"]
        person = create_person(repository, person_input)
        return cls(ok=True, person_id=person.id)
