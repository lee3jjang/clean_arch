from dp.domain.person.repository.protocol import PersonRepositoryProtocol
from dp.domain.person.model import Person
from dp.domain.person.dto import PersonDto


def list_person(repository: PersonRepositoryProtocol) -> list[Person]:
    return repository.list_person()


def create_person(
    repository: PersonRepositoryProtocol,
    person_dto: PersonDto,
) -> Person:
    return repository.create_person(person_dto)


def get_person(
    repository: PersonRepositoryProtocol,
    person_id: str,
) -> Person:
    return repository.get_person(person_id)


def edit_person(
    repository: PersonRepositoryProtocol,
    person_id: str,
    person_dto: PersonDto,
) -> None:
    return repository.edit_person(person_id, person_dto)


def delete_person(
    repository: PersonRepositoryProtocol,
    person_id: str,
) -> None:
    return repository.delete_person(person_id)
