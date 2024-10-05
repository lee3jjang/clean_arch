from dp.domain.person.repository import PersonRepository
from dp.domain.person.base_model import Person
from dp.domain.person.dto import PersonDto


def list_person(repository: PersonRepository) -> list[Person]:
    return repository.list_person()


def create_person(
    repository: PersonRepository,
    person_dto: PersonDto,
) -> Person:
    return repository.create_person(person_dto)


def get_person(
    repository: PersonRepository,
    person_id: str,
) -> Person:
    return repository.get_person(person_id)


def edit_person(
    repository: PersonRepository,
    person_id: str,
    person_dto: PersonDto,
) -> None:
    return repository.edit_person(person_id, person_dto)


def delete_person(
    repository: PersonRepository,
    person_id: str,
) -> None:
    return repository.delete_person(person_id)
