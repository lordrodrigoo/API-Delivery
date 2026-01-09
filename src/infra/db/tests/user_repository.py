from typing import List
from src.domain.models.user import Users

class UserRepositorySpy:
    def __init__(self) -> None:
        self.insert_user_attributes = {}
        self.select_user_attributes = {}

    def insert_user(
        self,
        first_name: str,
        last_name: str,
        password_hash: str,
        age: int,
        phone: str,
        email: str,
        is_active: bool,
        created_at: str,
        updated_at: str
    ) -> Users:
        self.insert_user_attributes["first_name"] = first_name
        self.insert_user_attributes["last_name"] = last_name
        self.insert_user_attributes["password_hash"] = password_hash
        self.insert_user_attributes["age"] = age
        self.insert_user_attributes["phone"] = phone
        self.insert_user_attributes["email"] = email
        self.insert_user_attributes["is_active"] = is_active
        self.insert_user_attributes["created_at"] = created_at
        self.insert_user_attributes["updated_at"] = updated_at

    def select_user(self, first_name: str) -> List[Users]:
        self.select_user_attributes["first_name"] = first_name
        return [
            Users(
                id=1,
                first_name="John",
                last_name="Doe",
                age=30,
                email="john.doe@example.com",
                password_hash="hashed_password",
                phone="1234567890",
                is_active=True,
                created_at="2024-01-01T00:00:00",
                updated_at=None
            )
        ]
