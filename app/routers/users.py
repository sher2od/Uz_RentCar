from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate,UserResponse
from app.services.user_service import create_user

from app.dependencies import get_db

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.post("/",response_model=UserResponse)
def create_new_user(user:UserCreate,db:Session = Depends(get_db)):
    return create_user(db,user)