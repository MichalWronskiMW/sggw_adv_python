from enum import Enum


class FuelType(str, Enum):
    Gasoline = "Gasoline"
    Diesel = "Diesel"
    Electric = "Electric"
    Hybrid = "Hybrid"
    Other = "Other"
    Flexible_Fuel = "Flexible Fuel"


class SellerType(str, Enum):
    Insurance = "Insurance"
    Non_Insurance = "Non-Insurance"
