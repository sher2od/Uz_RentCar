# from typing import List, Optional
# from pydantic import BaseModel
# from enum import Enum


# # ======================
# # ENUMLAR
# # ======================

# class EngineType(str, Enum):
#     MECHANIC = "MECHANIC"
#     AUTOMATIC = "AUTOMATIC"
#     AUTOMAT = "AUTOMAT"  # <-- aynan bazadagi enum qiymatlar bilan bir xil

# class FuelType(str, Enum):
#     PETROL = "petrol"
#     DIESEL = "diesel"
#     ELECTRIC = "electric"
#     HYBRID = "hybrid"

# class ShapeType(str, Enum):
#     sedan = "sedan"
#     suv = "suv"
#     hatchback = "hatchback"
#     coupe = "coupe"
#     pickup = "pickup"


# # ======================
# # IMAGE va EQUIPMENT SCHEMALAR
# # ======================

# class ImageBase(BaseModel):
#     url: str


# class ImageResponse(ImageBase):
#     id: int

#     class Config:
#         orm_mode = True
#         from_attributes = True


# class EquipmentBase(BaseModel):
#     name: str


# class EquipmentResponse(EquipmentBase):
#     id: int

#     class Config:
#         orm_mode = True
#         from_attributes = True


# # ======================
# # CAR SCHEMALAR
# # ======================

# class CarBase(BaseModel):
#     model: str
#     brand: str
#     price: float
#     engine_type: EngineType
#     doors: int
#     fuel_type: FuelType
#     air_condition: bool = True
#     shape_type: ShapeType
#     distance: int
#     is_available: bool = True


# # 🟢 Yangi mashina yaratish
# class CarCreate(CarBase):
#     images: Optional[List[ImageBase]] = []
#     equipments: Optional[List[EquipmentBase]] = []


# # 🟡 Mavjud mashinani yangilash
# class CarUpdate(BaseModel):
#     model: Optional[str] = None
#     brand: Optional[str] = None
#     price: Optional[float] = None
#     engine_type: Optional[EngineType] = None
#     doors: Optional[int] = None
#     fuel_type: Optional[FuelType] = None
#     air_condition: Optional[bool] = None
#     shape_type: Optional[ShapeType] = None
#     distance: Optional[int] = None
#     is_available: Optional[bool] = None


# # 🔵 Bitta mashinani o‘qish uchun
# class CarResponse(BaseModel):
#    class CarResponse(BaseModel):
#     id: int
#     model: str
#     brand: str
#     price: float
#     engine_type: EngineType
#     doors: int
#     fuel_type: FuelType
#     air_condition: bool
#     shape_type: Optional[ShapeType] = None  # 🔧 NULL holatlarda xato chiqmasin
#     distance: int
#     is_available: bool
#     images: List[ImageResponse] = []
#     equipments: List[EquipmentResponse] = []

#     class Config:
        
#         from_attributes = True


# # 🔴 Bir nechta mashinalarni o‘qish uchun
# class CarsResponse(BaseModel):
#     cars: List[CarResponse]

#     class Config:
       
#         from_attributes = True


from typing import List, Optional
from pydantic import BaseModel
from enum import Enum


# ======================
# ENUMLAR
# ======================

class EngineType(str, Enum):
    MECHANIC = "MECHANIC"
    AUTOMATIC = "AUTOMATIC"
    AUTOMAT = "AUTOMAT"  # <-- bazadagi qiymatlar bilan bir xil


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


# ======================
# IMAGE va EQUIPMENT SCHEMALAR
# ======================

class ImageBase(BaseModel):
    url: str


class ImageResponse(ImageBase):
    id: int

    class Config:
        from_attributes = True  # ✅ orm_mode o‘rniga shu ishlatiladi


class EquipmentBase(BaseModel):
    name: str


class EquipmentResponse(EquipmentBase):
    id: int

    class Config:
        from_attributes = True


# ======================
# CAR SCHEMALAR
# ======================

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


# 🟢 Yangi mashina yaratish
class CarCreate(CarBase):
    images: Optional[List[ImageBase]] = []
    equipments: Optional[List[EquipmentBase]] = []


# 🟡 Mavjud mashinani yangilash
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


# 🔵 Bitta mashinani o‘qish uchun
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


# 🔴 Bir nechta mashinalarni o‘qish uchun
class CarsResponse(BaseModel):
    cars: List[CarResponse]

    class Config:
        from_attributes = True
