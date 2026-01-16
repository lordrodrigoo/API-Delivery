# pylint: disable=redefined-builtin
from datetime import datetime
from dataclasses import dataclass
from typing import Optional

@dataclass
class Account:
    """Entity of domain - it represents an account in the system."""
    id: str
    user_id: int
    username: str
    password_hash: str
    status: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    @property
    def is_active(self) -> bool:
        """Returns the active status of the account."""
        return self.status

    @staticmethod
    def create_account(
        id: int,
        user_id: int,  # Foreign key to Users
        username: str,
        password_hash: str,
        status: bool
    ) -> 'Account':
        """Factory method to create a new account instance."""
        return Account(
            id=id,
            user_id=user_id,
            username=username,
            password_hash=password_hash,
            status=status
        )

    @staticmethod
    def from_entity(entity) -> 'Account':
        """Converts an AccountEntity to an Account domain model."""
        return Account(
            id=entity.id,
            user_id=entity.user_id,
            username=entity.username,
            password_hash=entity.password_hash,
            status=entity.status,
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )
