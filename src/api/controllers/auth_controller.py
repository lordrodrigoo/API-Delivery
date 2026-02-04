import os
from dotenv import load_dotenv
from passlib.context import CryptContext
from fastapi import APIRouter
from src.dto.request.auth_user_request import AuthUserRequest
from src.dto.response.auth_user_response import AuthUserResponse
from src.usecases.auth_user_usecases import AuthUserUsecase
from src.infra.db.repositories.user_repository_interface import UserRepository
from src.infra.db.repositories.account_user_repository_interface import AccountRepository
from src.infra.db.settings.connection import DBConnectionHandler

load_dotenv()
API_PREFIX = os.getenv("API_V1_AUTH")
TAG = os.getenv("TAG_AUTH")
router = APIRouter(prefix=API_PREFIX, tags=[TAG])


db_handler = DBConnectionHandler()
user_repository = UserRepository(db_handler)
account_repository = AccountRepository(db_handler)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
auth_usecase = AuthUserUsecase(user_repository, account_repository, pwd_context)

@router.post("/login", response_model=AuthUserResponse)
def login(auth_request: AuthUserRequest):
    """Endpoint to authenticate a user and provide a JWT token."""
    return auth_usecase.authenticate_user(auth_request)
