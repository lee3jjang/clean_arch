from typing import Protocol

from graphene import InputObjectType, ObjectType, ID, String  # type: ignore[import-untyped]


class HasNameProtocol(Protocol):
    name: str


class PersonObjectType(ObjectType):
    id = ID()
    name = String(required=True)

    @staticmethod
    def resolve_name(parent: HasNameProtocol, info) -> str:
        return parent.name


class PersonInputObjectType(InputObjectType):
    name = String(required=True)


PERSON_TYPES = [
    PersonObjectType,
]
