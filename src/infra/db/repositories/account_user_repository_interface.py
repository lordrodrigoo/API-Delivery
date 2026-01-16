from typing import List, Optional
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.account import AccountEntity
from src.domain.repositories.account_repository import AccountRepositoryInterface
from src.domain.models.account import Account

class AccountRepository(AccountRepositoryInterface):

    @classmethod
    def create_account(cls, account: Account) -> Account:
        """Creates a new account in database"""
        with DBConnectionHandler() as db_connection:
            try:
                now = datetime.now()
                new_account = AccountEntity(
                    id = account.id,
                    user = account.user_id,
                    username = account.username,
                    password_hash = account.password_hash,
                    status = account.status,
                    created_at = now,
                    updated_at = now
                )
                db_connection.session.add(new_account)
                db_connection.session.commit()
                db_connection.session.refresh(new_account)

                return Account.from_entity(new_account)

            except SQLAlchemyError as error:
                db_connection.session.rollback()
                raise error

    @classmethod
    def update_account(cls, account: Account) -> Optional[Account]:
        """Updates an existing account in the database."""
        if account.id is None:
            raise ValueError("Account ID must be provided for update.")

        with DBConnectionHandler() as db_connection:
            try:
                existing_account = (
                    db_connection.session
                    .query(AccountEntity)
                    .filter(AccountEntity.id == account.id)
                    .first()
                )

                if not existing_account:
                    return None

                # Update all fields
                existing_account.user_id = account.user_id
                existing_account.username = account.username
                existing_account.password_hash = account.password_hash
                existing_account.status = account.status
                existing_account.updated_at = datetime.now()

                db_connection.session.commit()
                db_connection.session.refresh(existing_account)

                return Account.from_entity(existing_account)

            except SQLAlchemyError as error:
                db_connection.session.rollback()
                raise error

    @classmethod
    def find_all_accounts(cls) -> List[Account]:
        """Retrieves all accounts from the database."""
        with DBConnectionHandler() as db_connection:
            try:
                accounts_entities = db_connection.session.query(AccountEntity).all()
                return [Account.from_entity(entity) for entity in accounts_entities]

            except SQLAlchemyError as error:
                raise error

    @classmethod
    def find_account_by_id(cls, account_id: str) -> Optional[Account]:
        """Finds an account by its ID."""
        with DBConnectionHandler() as db_connection:
            try:
                account_entity = (
                    db_connection.session
                    .query(AccountEntity)
                    .filter(AccountEntity.id == account_id)
                    .first()
                )

                if account_entity:
                    return Account.from_entity(account_entity)
                return None

            except SQLAlchemyError as error:
                raise error

