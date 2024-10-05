from typing import cast
from psycopg2._psycopg import connection  # type: ignore[import-untyped]

from dp.domain.person.model import Person
from dp.domain.person.dto import PersonDto


class PersonDatabaseRepository:
    def __init__(self, connection: connection) -> None:
        self.connection = connection
        self.cursor = connection.cursor()

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
