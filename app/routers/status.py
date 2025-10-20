from typing import Annotated
from fastapi.routing import APIRouter
from fastapi import Depends, Path, status, HTTPException, Body
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
import jwt

from app.dependencies import get_db
from app.models.user import User, UserRoles
from app.models.car import Car
from app.models.order import Order
from app.schemas.order import OrdersResponse
from app.core.config import SECRET_KEY, JWT_ALGORITHM

router = APIRouter(
    prefix='/admin',
    tags=['Admin Endpoints']
)

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/users/login")

#  Admin statistikasi
@router.get('/')
async def get_admin_stats(
    db: Annotated[Session, Depends(get_db)],
    token: Annotated[str, Depends(oauth2_schema)]
):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
    user_id = int(payload['sub'])

    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist.")
    if user.role != UserRoles.admin:
        raise HTTPException(status_code=403, detail="Permission denied.")

    return {
        "users": db.query(User).count(),
        "cars": db.query(Car).count(),
        "orders": db.query(Order).count()
    }

# Barcha buyurtmalarni olish
@router.get('/orders', response_model=OrdersResponse)
async def get_all_orders_admin(
    db: Annotated[Session, Depends(get_db)],
    token: Annotated[str, Depends(oauth2_schema)]
):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
    user_id = int(payload['sub'])

    user = db.query(User).filter_by(id=user_id).first()
    if not user or user.role != UserRoles.admin:
        raise HTTPException(status_code=403, detail="Permission denied.")

    orders = db.query(Order).all()
    return OrdersResponse(orders=orders)

#  Buyurtma statusini yangilash
@router.put('/orders/{order_id}/status')
async def update_order_status(
    order_id: int,
    status: Annotated[str, Body(embed=True)],
    db: Annotated[Session, Depends(get_db)],
    token: Annotated[str, Depends(oauth2_schema)]
):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
    user_id = int(payload['sub'])

    user = db.query(User).filter_by(id=user_id).first()
    if not user or user.role != UserRoles.admin:
        raise HTTPException(status_code=403, detail="Permission denied.")

    order = db.query(Order).filter_by(id=order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found.")

    if status not in ["pending", "accepted", "cancelled"]:
        raise HTTPException(status_code=400, detail="Invalid status value. Use: pending, accepted, cancelled")

    order.status = status
    db.commit()
    db.refresh(order)

    return {"message": f"Order #{order_id} status changed to '{status}' ✅"}
