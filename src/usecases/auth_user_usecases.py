from passlib.context import CryptContext
from src.dto.request.auth_user_request import AuthUserRequest
from src.dto.response.auth_user_response import AuthUserResponse
from src.domain.repositories.account_repository import AccountRepositoryInterface
from src.domain.repositories.user_repository import UserRepositoryInterface
from src.exceptions.exception_handlers import InvalidCredentialsException
from src.auth.jwt_handler import create_access_token

class AuthUserUsecase:
    def __init__(
        self,
        user_repository: UserRepositoryInterface,
        account_repository: AccountRepositoryInterface,
        pwd_context: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")
    ):
        self.user_repository = user_repository
        self.account_repository = account_repository
        self.pwd_context = pwd_context


    def authenticate_user(self, auth_request: AuthUserRequest) -> AuthUserResponse:
        # Search for account by username
        account = self.account_repository.find_by_username(auth_request.username)

        if not account or not self.pwd_context.verify(auth_request.password, account.password_hash):
            raise InvalidCredentialsException()
        # Search user vinculated to account
        user = self.user_repository.find_user_by_id(account.user_id)

        if not user:
            raise InvalidCredentialsException()
        # Create JWT token
        token = create_access_token({"sub": str(user.id)})

        return AuthUserResponse(access_token=token, token_type="bearer")
