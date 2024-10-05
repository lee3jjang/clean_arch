import psycopg2  # type: ignore[import-untyped]

DB = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="example",
    dbname="db",
)
