from fastapi import Depends, HTTPException, status
from src.auth.security import oauth2_scheme
from src.auth.jwt_handler import verify_access_token
from src.infra.db.repositories.user_repository_interface import UserRepository


def get_current_user(
        token: str = Depends(oauth2_scheme),
        user_repository: UserRepository = Depends()
    ) -> dict:


    payload = verify_access_token(token)
    if payload is None or "user_id" not in payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing Token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = user_repository.find_user_by_id(payload["user_id"])
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
