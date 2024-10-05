from sqlalchemy import select, Engine
from sqlalchemy.orm import Session

from dp.domain.person.model import Person
from dp.domain.person.dto import PersonDto
from dp.domain.person.entity import PersonEntity


class PersonOrmRepository:
    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def list_person(self) -> list[Person]:
        stmt = select(PersonEntity)
        with Session(self.engine) as session:
            return [
                Person(id=str(person_entity.id), name=person_entity.name)
                for person_entity in session.scalars(stmt)
            ]

    def create_person(self, person_dto: PersonDto) -> Person:
        with Session(self.engine) as session:
            person_entity = PersonEntity(name=person_dto["name"])
            session.add(person_entity)
            session.commit()

            return Person(id=str(person_entity.id), name=person_entity.name)

    def get_person(self, person_id: str) -> Person:
        with Session(self.engine) as session:
            person_entity = session.get(PersonEntity, person_id)
            if person_entity is None:
                raise ValueError("Person not found")
            return Person(id=str(person_entity.id), name=person_entity.name)

    def edit_person(self, person_id: str, person_dto: PersonDto) -> None:
        with Session(self.engine) as session:
            person_entity = session.get(PersonEntity, person_id)
            if person_entity is None:
                raise ValueError("Person not found")
            person_entity.name = person_dto["name"]
            session.commit()

    def delete_person(self, person_id: str) -> None:
        with Session(self.engine) as session:
            person_entity = session.get(PersonEntity, person_id)
            if person_entity:
                session.delete(person_entity)
                session.commit()
