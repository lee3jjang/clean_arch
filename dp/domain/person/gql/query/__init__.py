from .person_list_query import PersonListQuery  # type: ignore[import-untyped, import-not-found]
from .person_query import PersonQuery  # type: ignore[import-untyped, import-not-found]


class PersonQueries(
    PersonListQuery,
    PersonQuery,
):
    pass
