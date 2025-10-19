

from typing import List, Optional
from pydantic import BaseModel
from enum import Enum




class EngineType(str, Enum):
    MECHANIC = "MECHANIC"
    AUTOMATIC = "AUTOMATIC"
    AUTOMAT = "AUTOMAT" 


class FuelType(str, Enum):
    PETROL = "petrol"
    DIESEL = "diesel"
    ELECTRIC = "electric"
    HYBRID = "hybrid"


class ShapeType(str, Enum):
    sedan = "sedan"
    suv = "suv"
    hatchback = "hatchback"
    coupe = "coupe"
    pickup = "pickup"



class ImageBase(BaseModel):
    url: str


class ImageResponse(ImageBase):
    id: int

    class Config:
        from_attributes = True  


class EquipmentBase(BaseModel):
    name: str


class EquipmentResponse(EquipmentBase):
    id: int

    class Config:
        from_attributes = True




class CarBase(BaseModel):
    model: str
    brand: str
    price: float
    engine_type: EngineType
    doors: int
    fuel_type: FuelType
    air_condition: bool = True
    shape_type: ShapeType
    distance: int
    is_available: bool = True



class CarCreate(CarBase):
    images: Optional[List[ImageBase]] = []
    equipments: Optional[List[EquipmentBase]] = []



class CarUpdate(BaseModel):
    model: Optional[str] = None
    brand: Optional[str] = None
    price: Optional[float] = None
    engine_type: Optional[EngineType] = None
    doors: Optional[int] = None
    fuel_type: Optional[FuelType] = None
    air_condition: Optional[bool] = None
    shape_type: Optional[ShapeType] = None
    distance: Optional[int] = None
    is_available: Optional[bool] = None



class CarResponse(BaseModel):
    id: int
    model: str
    brand: str
    price: float
    engine_type: EngineType
    doors: int
    fuel_type: FuelType
    air_condition: bool
    shape_type: Optional[ShapeType] = None  # NULL bo‘lsa ham ishlaydi
    distance: int
    is_available: bool
    images: List[ImageResponse] = []
    equipments: List[EquipmentResponse] = []

    class Config:
        from_attributes = True


class CarsResponse(BaseModel):
    cars: List[CarResponse]

    class Config:
        from_attributes = True
