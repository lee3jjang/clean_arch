from uuid import uuid4

from typing import Protocol

from dp.domain.person.base_model import Person
from dp.domain.person.dto import PersonDto


class PersonRepository(Protocol):
    def list_person(self) -> list[Person]: ...

    def create_person(self, person_dto: PersonDto) -> Person: ...

    def get_person(self, person_id: str) -> Person: ...

    def edit_person(self, person_id: str, person_dto: PersonDto) -> None: ...

    def delete_person(self, person_id: str) -> None: ...


class PersonInMemoryRepository:
    persons: list[Person]

    def __init__(self) -> None:
        self.persons: list[Person] = []

    def list_person(self) -> list[Person]:
        return self.persons

    def create_person(self, person_dto: PersonDto) -> Person:
        person_id = str(uuid4())
        person = Person(id=person_id, **person_dto)
        self.persons.append(person)
        return person

    def get_person(self, person_id: str) -> Person:
        person = list(
            filter(
                lambda person: person.id == person_id,
                self.persons,
            ),
        )[0]
        return person

    def edit_person(self, person_id: str, person_dto: PersonDto) -> None:
        person = self.get_person(person_id)
        person.name = person_dto["name"]

    def delete_person(self, person_id: str) -> None:
        person = self.get_person(person_id)
        self.persons.remove(person)
