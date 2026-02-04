#pylint: disable=redefined-outer-name
from unittest.mock import MagicMock
import pytest
from src.usecases.user_usecases import CreateUserUsecase


@pytest.fixture
def valid_user_data():
    return {
        "first_name": "Rodrigo",
        "last_name": "Souza",
        "age": 30,
        "email": "rodrigo.souza@example.com",
        "phone": "11999999999",
        "password": "@1234StrongPass",
        "username": "rodrigo.souza"
    }


@pytest.fixture
def user_repository_mock():
    return MagicMock()

@pytest.fixture
def account_repository_mock():
    return MagicMock()

@pytest.fixture
def usecase(user_repository_mock, account_repository_mock):
    return CreateUserUsecase(user_repository_mock, account_repository_mock)
