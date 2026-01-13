#pylint: disable=unused-import
#pylint: disable=redefined-outer-name
from datetime import datetime
import pytest
from src.infra.db.repositories.user_repository import UserRepository
from src.infra.db.tests.helpers.connection_db import db_connection, teardown

@pytest.fixture
def user_repository():
    return UserRepository()

@pytest.fixture
def user_data():
    return {
        'first_name': 'John',
        'last_name': 'Doe',
        'password_hash': 'hashed_password',
        'age': 30,
        'phone': '123-456-7890',
        'email': 'john.doe@example.com',
        'is_active': True,
        'created_at': datetime.now(),
        'updated_at': datetime.now()
    }

sql_del = "TRUNCATE TABLE users RESTART IDENTITY CASCADE;"

class TestUserRepository:

    def test_insert_user(self, user_repository, user_data):
        user_repository.insert_user(**user_data)
        user = user_repository.select_user(user_data['first_name'])[0]
        assert user.first_name == user_data['first_name']
        assert user.last_name == user_data['last_name']
        assert user.age == user_data['age']

    def test_select_user(self, user_repository, user_data, teardown):
        user_repository.insert_user(**user_data)
        user = user_repository.select_user(user_data['first_name'])[0]
        assert user.first_name == user_data['first_name']
        assert user.last_name == user_data['last_name']
        assert user.age == user_data['age']
        assert user.email == user_data['email']
        teardown(sql_del)  # Remove after new tests
