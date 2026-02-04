import os
from dotenv import load_dotenv
from fastapi import APIRouter, Depends
from src.auth.dependencies import get_current_user
from src.usecases.user_usecases import CreateUserUsecase
from src.infra.db.repositories.user_repository_interface import UserRepository
from src.infra.db.repositories.account_user_repository_interface import AccountRepository
from src.infra.db.settings.connection import DBConnectionHandler
from src.dto.request.user_request import CreateUserRequest
from src.dto.response.user_response import UserResponse

load_dotenv()
API_PREFIX = os.getenv("API_V1_USER")
TAG = os.getenv("TAG_USER")
router = APIRouter(prefix=API_PREFIX, tags=[TAG])

db_handler = DBConnectionHandler()
user_repository = UserRepository(db_handler)
account_repository = AccountRepository(db_handler)
create_user_usecase = CreateUserUsecase(user_repository, account_repository)


@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user_request: CreateUserRequest):
    """Endpoint to create a new user."""
    return create_user_usecase.create_user(user_request)


@router.get("/me")
def read_users_me(current_user=Depends(get_current_user)):
    """Endpoint to get the current logged-in user."""
    return current_user
