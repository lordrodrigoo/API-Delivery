import re
from pydantic import BaseModel, Field, field_validator

class AuthUserRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8)

    @field_validator("username")
    @classmethod
    def username_must_be_alphanumeric(cls, username: str) -> str:
        if not username.isalnum():
            raise ValueError("username must be alphanumeric")
        return username

    @field_validator("password")
    @classmethod
    def password_strength(cls, password: str) -> str:
        pattern = r'^(?=.*[A-Z])(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        if not re.match(pattern, password):
            raise ValueError(
                "Password must contain at least one uppercase letter and one special character"
            )
        return password
