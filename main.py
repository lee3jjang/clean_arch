import os

import psycopg2  # type: ignore[import-untyped]
from flask import Flask
from flask_graphql.graphqlview import GraphQLView  # type: ignore[import-untyped]
from dotenv.main import load_dotenv

load_dotenv()

from dp.schema import schema  # type: ignore[import-untyped]

DATABASE_URL = os.environ.get("DATABASE_URL", "")


app = Flask(__name__)

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        name="graphql",
        schema=schema,
        graphiql=True,
    ),
)


def initialize() -> None:
    from sqlalchemy import create_engine

    from dp.repository import REPOSITORY
    from dp.base import Base

    from dp.domain.person.repository.person_database_repository import (
        PersonDatabaseRepository,
    )

    # from dp.domain.person.repository.person_orm_repository import PersonOrmRepository
    # from dp.domain.person.repository.person_in_memory_repository import (
    #     PersonInMemoryRepository,
    # )

    # Initialize orm
    engine = create_engine(DATABASE_URL, echo=True)
    Base.metadata.create_all(engine)

    # # Initialize connection
    connection = psycopg2.connect(DATABASE_URL)

    # Initialize repositories
    REPOSITORY["person"] = PersonDatabaseRepository(connection)
    # REPOSITORY["person"] = PersonOrmRepository(engine)
    # REPOSITORY["person"] = PersonInMemoryRepository()


if __name__ == "__main__":
    initialize()

    app.run(debug=True)
