from graphene import ObjectType, Schema  # type: ignore[import-untyped]

from dp.domain.person.gql.object_type import PERSON_TYPES  # type: ignore[import-untyped]
from dp.domain.person.gql.query import PersonQueries  # type: ignore[import-untyped]
from dp.domain.person.gql.mutation import PersonMutations  # type: ignore[import-untyped]


class Query(
    ObjectType,
    PersonQueries,
):
    pass


class Mutation(
    ObjectType,
    PersonMutations,
):
    pass


schema = Schema(
    query=Query,
    mutation=Mutation,
    types=[
        *PERSON_TYPES,
    ],
)
