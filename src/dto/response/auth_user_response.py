from pydantic import BaseModel

class AuthUserResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    refresh_token: str | None = None
