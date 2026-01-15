from typing import Optional
from pydantic.dataclasses import dataclass
from .enums import FuelType, SellerType

@dataclass
class VehicleInput:
    stock_number: str
    year: int
    make: str
    model: str
    vin: str

    current_bid: Optional[float]
    odometer: Optional[int]

    fuel_type: Optional[FuelType]
    seller_type: Optional[SellerType]
    transmission: Optional[str] = None
    drive_line: Optional[str] = None
    body_style: Optional[str] = None
    primary_damage: Optional[str] = None
    secondary_damage: Optional[str] = None
