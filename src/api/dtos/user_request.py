from pydantic import BaseModel, EmailStr, Field



class CreateUserRequest(BaseModel):
    # ... means required field
    # property ge means greater than or equal to
    # property le means less than or equal to
    first_name: str = Field(..., min_length=3, max_length=25, description="Your first name")
    last_name: str = Field(..., min_length=3, max_length=25, description="Your last name")
    age: int = Field(..., ge=16, le=100, description="Your age")
    email: EmailStr = Field(..., description="Your email address")
    phone: str = Field(..., min_length=10, max_length=15, description="Your phone number")
    password: str = Field(..., min_length=8, description="Your password")
