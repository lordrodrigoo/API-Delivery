from typing import List, Optional
from sqlalchemy.exc import SQLAlchemyError
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.user import UserEntity
from src.domain.repositories.user_repository import UserRepositoryInterface
from src.domain.models.user import Users
from src.utils.base_repository import BaseRepository


class UserRepository(UserRepositoryInterface, BaseRepository[UserEntity]):
    def __init__(self, db_connection: DBConnectionHandler):
        super().__init__(UserEntity, db_connection.get_session())

    def create_user(self, user: Users) -> Users:
        entity = UserEntity(
            first_name=user.first_name,
            last_name=user.last_name,
            age=user.age,
            email=user.email,
            password_hash=user.password_hash,
            phone=user.phone,
            is_active=user.is_active,
            created_at=user.created_at,
            updated_at=user.updated_at
        )
        self.add(entity)
        return Users.from_entity(entity)

    def update_user(self, user: Users) -> Users:
        entity = self.session.query(self.model).get(user.id)

        if entity:
            entity.first_name = user.first_name
            entity.last_name = user.last_name
            entity.age = user.age
            entity.email = user.email
            entity.password_hash = user.password_hash
            entity.phone = user.phone
            entity.is_active = user.is_active
            entity.updated_at = user.updated_at
            self.update(entity)

        return Users.from_entity(entity)

    def find_all_users(self) -> List[Users]:
        return [Users.from_entity(user) for user in self.get_all()]

    def find_user_by_id(self, user_id: int) -> Optional[Users]:
        entity = self.get_by_id(user_id)
        return Users.from_entity(entity) if entity else None

    def find_by_name(self, name: str) -> List[Users]:
        entities = self.session.query(self.model).filter(self.model.first_name == name).all()
        return [Users.from_entity(user) for user in entities]

    def delete_user(self, user_id: int) -> bool:
        entity = self.get_by_id(user_id)

        if entity:
            self.delete(entity)
            return True
        return False

    def select_user_by_name(self, name: str) -> Optional[Users]:
        """Select a user by their name."""
        try:
            entity = self.get_by_name(name)
            if entity:
                return Users.from_entity(entity)
            return None
        except SQLAlchemyError as e:
            print(f"Database error occurred: {e}")
            return None
