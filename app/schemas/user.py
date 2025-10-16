from typing import Annotated
from enum import Enum

from pydantic import BaseModel,Field,EmailStr


class UserRoles(str,Enum):
    user = "user"
    admin = "admin"

class UserCreate(BaseModel):
    email: Annotated[str,EmailStr]
    password:Annotated[str,Field(min_length=8)]
    name:Annotated[str,Field(min_length=3)]
    phone:Annotated[str,Field(min_length=9,max_length=15)]

class UserResponse(BaseModel):
    id:int
    email: Annotated[str,EmailStr]
    name:Annotated[str,Field(min_length=3)]
    phone:Annotated[str,Field(min_length=9,max_length=15)]
    role:Annotated[str,UserRoles]
    is_verified:bool

    class Config:
        from_attributes = True
    
    



class VerificationCode(BaseModel):
    email: Annotated[str, EmailStr]
    code: Annotated[int, Field(ge=0, le=9999, example=0)]  

class UserLogin(BaseModel):
    email:Annotated[str,EmailStr]
    password:Annotated[str,Field(min_length=8)]
