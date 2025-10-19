from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from app.schemas.car import CarResponse, CarsResponse, CarCreate, CarUpdate
from app.models.car import Car, Image, Equipment
from app.dependencies import get_db

router = APIRouter(
    prefix="/cars",
    tags=["Cars Endpoints"]
)

# ========================
# GET ALL CARS
# ========================
@router.get('/', response_model=CarsResponse)
async def get_cars(db: Annotated[Session, Depends(get_db)]):
    cars = db.query(Car).all()
    data = []
    for car in cars:
        data.append({
            "id": car.id,
            "model": car.model,
            "brand": car.brand,
            "price": car.price,
            "engine_type": car.engine_type,
            "doors": car.doors,
            "fuel_type": car.fuel_type,
            "air_condition": car.air_condition,
            "shape_type": car.shape_type,
            "distance": car.distance,
            "is_available": car.is_available,
            "images": [{"id": img.id, "url": img.url} for img in car.images],
            "equipments": [{"id": e.id, "name": e.name} for e in car.equipments],
        })
    return {"cars": data}


# ========================
# GET ONE CAR
# ========================
@router.get("/{car_id}", response_model=CarResponse)
async def get_one_car(car_id: int, db: Annotated[Session, Depends(get_db)]):
    car = db.query(Car).filter(Car.id == car_id).first()
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car


# ========================
# ADD NEW CAR
# ========================
@router.post("/", response_model=CarResponse, status_code=status.HTTP_201_CREATED)
async def add_car(car_data: CarCreate, db: Annotated[Session, Depends(get_db)]):
    # 1️⃣ Yangi Car obyekt yaratamiz
    new_car = Car(
        model=car_data.model,
        brand=car_data.brand,
        price=car_data.price,
        engine_type=car_data.engine_type,
        doors=car_data.doors,
        fuel_type=car_data.fuel_type,
        air_condition=car_data.air_condition,
        shape_type=car_data.shape_type,
        distance=car_data.distance,
        is_available=car_data.is_available
    )

    # 2️⃣ DBga saqlaymiz
    db.add(new_car)
    db.commit()
    db.refresh(new_car)

    # 3️⃣ Rasmlar bo‘lsa — qo‘shamiz
    if car_data.images:
        for img in car_data.images:
            image = Image(url=img.url, car_id=new_car.id)
            db.add(image)

    # 4️⃣ Jihozlar bo‘lsa — qo‘shamiz
    if car_data.equipments:
        for eq in car_data.equipments:
            equipment = Equipment(name=eq.name, car_id=new_car.id)
            db.add(equipment)

    db.commit() 
    db.refresh(new_car)

    return new_car


# ========================
# UPDATE CAR
# ========================
@router.put("/{car_id}", response_model=CarResponse)
async def update_car(car_id: int, car_data: CarUpdate, db: Annotated[Session, Depends(get_db)]):
    car = db.query(Car).filter(Car.id == car_id).first()
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")

    # Faqat kiritilgan maydonlarni yangilaymiz
    for field, value in car_data.model_dump(exclude_unset=True).items():
        setattr(car, field, value)

    db.commit()
    db.refresh(car)
    return car


# ========================
# DELETE CAR
# ========================
@router.delete("/{car_id}")
async def delete_car(car_id: int, db: Annotated[Session, Depends(get_db)]):
    car = db.query(Car).filter(Car.id == car_id).first()
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")

    db.delete(car)
    db.commit()

    return {"detail": "Car o'chirildi"}














