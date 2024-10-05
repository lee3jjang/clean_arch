from typing import Self

from graphene import Mutation, ID, Boolean  # type: ignore[import-untyped]
from dp.repository import REPOSITORY
from dp.domain.person.service import delete_person


class DeletePersonMutation(Mutation):
    class Arguments:
        person_id = ID()

    ok = Boolean()

    @classmethod
    def mutate(cls, root, info, person_id: str) -> Self:
        repository = REPOSITORY["person"]
        delete_person(repository, person_id)
        return cls(ok=True)
