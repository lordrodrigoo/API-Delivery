from typing import List, Optional
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.user import UserEntity
from src.domain.repositories.user_repository import UserRepositoryInterface
from src.domain.models.user import Users


class UserRepository(UserRepositoryInterface):

    @classmethod
    def create_user(cls, user: Users) -> Users:
        """Creates a new user in database"""
        with DBConnectionHandler() as db_connection:
            try:
                now = datetime.now()
                new_user = UserEntity(
                    first_name=user.first_name,
                    last_name=user.last_name,
                    password_hash=user.password_hash,
                    age=user.age,
                    phone=user.phone,
                    email=user.email,
                    is_active=user.is_active,
                    created_at=now,
                    updated_at=now
                )
                db_connection.session.add(new_user)
                db_connection.session.commit()
                db_connection.session.refresh(new_user)

                return Users.from_entity(new_user)

            except SQLAlchemyError as error:
                db_connection.session.rollback()
                raise error

    @classmethod
    def update_user(cls, user: Users) -> Optional[Users]:
        """Updates an existing user in the database."""
        if user.id is None:
            raise ValueError("User ID must be provided for update.")

        with DBConnectionHandler() as db_connection:
            try:
                existing_user = (
                    db_connection.session
                    .query(UserEntity)
                    .filter(UserEntity.id == user.id)
                    .first()
                )

                if not existing_user:
                    return None

                # Update all fields
                existing_user.first_name = user.first_name
                existing_user.last_name = user.last_name
                existing_user.password_hash = user.password_hash
                existing_user.age = user.age
                existing_user.phone = user.phone
                existing_user.email = user.email
                existing_user.is_active = user.is_active
                existing_user.updated_at = datetime.now()

                db_connection.session.commit()
                db_connection.session.refresh(existing_user)

                return Users.from_entity(existing_user)

            except SQLAlchemyError as error:
                db_connection.session.rollback()
                raise error

    @classmethod
    def find_all(cls) -> List[Users]:
        """Return all users from database."""
        with DBConnectionHandler() as db_connection:
            try:
                entities = db_connection.session.query(UserEntity).all()
                return [Users.from_entity(entity) for entity in entities]

            except SQLAlchemyError as error:
                db_connection.session.rollback()
                raise error

    @classmethod
    def find_by_id(cls, user_id: int) -> Optional[Users]:
        """Search for a user by ID."""
        with DBConnectionHandler() as db_connection:
            try:
                entity = (
                    db_connection.session
                    .query(UserEntity)
                    .filter(UserEntity.id == user_id)
                    .first()
                )
                return Users.from_entity(entity) if entity else None

            except SQLAlchemyError as error:
                db_connection.session.rollback()
                raise error

    @classmethod
    def find_by_name(cls, name: str) -> List[Users]:
        """Search for users by name."""
        with DBConnectionHandler() as db_connection:
            try:
                entities = (
                    db_connection.session
                    .query(UserEntity)
                    .filter(UserEntity.first_name == name)
                    .all()
                )
                return [Users.from_entity(entity) for entity in entities]

            except SQLAlchemyError as error:
                db_connection.session.rollback()
                raise error

    @classmethod
    def delete_user(cls, user_id: int) -> bool:
        with DBConnectionHandler() as db_connection:
            try:
                entity = (
                    db_connection.session
                    .query(UserEntity)
                    .filter(UserEntity.id == user_id)
                    .first()
                )

                if not entity:
                    return False

                db_connection.session.delete(entity)
                db_connection.session.commit()
                return True

            except SQLAlchemyError as error:
                db_connection.session.rollback()
                raise error
