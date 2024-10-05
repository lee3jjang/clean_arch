from uuid import uuid4

from typing import Protocol, cast, Any

from dp.domain.person.base_model import Person
from dp.domain.person.dto import PersonDto


class PersonRepository(Protocol):
    def list_person(self) -> list[Person]: ...

    def create_person(self, person_dto: PersonDto) -> Person: ...

    def get_person(self, person_id: str) -> Person: ...

    def edit_person(self, person_id: str, person_dto: PersonDto) -> None: ...

    def delete_person(self, person_id: str) -> None: ...


class PersonDatabaseRepository:
    def __init__(self) -> None:
        from dp.db import DB

        self.connection = DB
        self.cursor = DB.cursor()

    def list_person(self) -> list[Person]:
        sql = "SELECT id, name FROM person"
        self.cursor.execute(sql)
        rows = cast(list[tuple[int, str]], self.cursor.fetchall())
        return [Person(id=str(row[0]), name=row[1]) for row in rows]

    def create_person(self, person_dto: PersonDto) -> Person:
        keys = ", ".join(person_dto.keys())
        values = ", ".join([f"'{value}'" for value in person_dto.values()])
        sql = (
            "INSERT INTO person ({keys}) VALUES ({values}) RETURNING id, {keys}".format(
                keys=keys, values=values
            )
        )
        self.cursor.execute(sql)
        self.connection.commit()

        row = self.cursor.fetchone()
        return Person(
            id=str(row[0]),
            **{key: row[i + 1] for i, key in enumerate(person_dto.keys())},
        )

    def get_person(self, person_id: str) -> Person:
        sql = "SELECT id, name FROM person where id={person_id}".format(
            person_id=person_id
        )
        self.cursor.execute(sql)
        row = cast(tuple[int, str], self.cursor.fetchone())
        return Person(id=str(row[0]), name=row[1])

    def edit_person(self, person_id: str, person_dto: PersonDto) -> None:
        items = ", ".join([f"{key}='{value}'" for key, value in person_dto.items()])
        sql = "UPDATE person SET {items} where id={person_id}".format(
            person_id=person_id,
            items=items,
        )
        self.cursor.execute(sql)
        self.connection.commit()

    def delete_person(self, person_id: str) -> None:
        sql = "DELETE FROM person where id = {person_id}".format(person_id=person_id)
        self.cursor.execute(sql)
        self.connection.commit()


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
