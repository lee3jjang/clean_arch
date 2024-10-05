from flask import Flask
from flask_graphql.graphqlview import GraphQLView  # type: ignore[import-untyped]

from dp.schema import schema  # type: ignore[import-untyped]


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
    from dp.settings import REPOSITORIES
    from dp.domain.person.repository import PersonDatabaseRepository

    # from dp.domain.person.repository import PersonInMemoryRepository

    # REPOSITORIES["person_repository"] = PersonInMemoryRepository()
    REPOSITORIES["person_repository"] = PersonDatabaseRepository()


if __name__ == "__main__":
    initialize()

    app.run(debug=True)
