from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List
from .enums import FuelType, SellerType


@dataclass
class Vehicle:
    stock_number: str
    year: int
    make: str
    model: str
    vin: str

    current_bid: Optional[float]
    odometer: Optional[int]

    fuel_type: Optional[FuelType]
    seller_type: Optional[SellerType]
    transmission: Optional[str]
    drive_line: Optional[str]
    body_style: Optional[str]
    primary_damage: Optional[str]
    secondary_damage: Optional[str]


@dataclass
class Auction:
    auction_date: datetime
    branch_name: str
    timed_auction: bool
    vehicles: List[Vehicle]
