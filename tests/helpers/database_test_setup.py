import os
from testcontainers.postgres import PostgresContainer


class DatabaseTestSetup:
    @staticmethod
    def start_postgres():
        postgres = PostgresContainer("postgres:16")
        postgres.start()

        os.environ["DB_HOST"] = postgres.get_container_host_ip()
        os.environ["DB_PORT"] = str(postgres.get_exposed_port(5432))
        os.environ["DB_USERNAME"] = postgres.username
        os.environ["DB_PASSWORD"] = postgres.password
        os.environ["DB_NAME"] = postgres.dbname
        return postgres

    @staticmethod
    def get_connection_url(container):
        """Returns the full connection string for the Postgres database."""
        return container.get_connection_url()

    @staticmethod
    def run_alembic_migrations():
        os.system("alembic upgrade head")

    @staticmethod
    def stop_postgres(container):
        container.stop()


