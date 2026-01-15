import pytest
from pydantic import ValidationError
from src.factory import VehicleFactory
from src.enums import FuelType, SellerType


def test_vehicle_validation_error():
    row = {
        "Stock Number": None,
        "Year": "not_a_year",
        "Make": "Toyota",
        "Model": "Corolla",
        "Vin#": "VIN123",
    }

    with pytest.raises(Exception):
        VehicleFactory.from_csv_row(row)


def test_vehicle_parsing_basic_fields():
    row = {
        "Stock Number": "123",
        "Year": "2020",
        "Make": "Toyota",
        "Model": "Camry",
        "Vin#": "TESTVIN",
        "Current Bid": "$10,500 USD",
        "Odometer": "100,000 mi",
        "Fuel Type": "Gasoline",
        "Seller Type": "Insurance",
    }

    vehicle = VehicleFactory.from_csv_row(row)

    assert vehicle.stock_number == "123"
    assert vehicle.year == 2020
    assert vehicle.make == "Toyota"
    assert vehicle.model == "Camry"
    assert vehicle.vin == "TESTVIN"


def test_vehicle_parsing_numbers():
    row = {
        "Stock Number": "999",
        "Year": "2015",
        "Make": "Ford",
        "Model": "Focus",
        "Vin#": "VIN123",
        "Current Bid": "$1,234 USD",
        "Odometer": "12,345 mi",
        "Fuel Type": "Gasoline",
        "Seller Type": "Insurance",
    }

    vehicle = VehicleFactory.from_csv_row(row)

    assert vehicle.current_bid == 1234.0
    assert vehicle.odometer == 12345


def test_vehicle_parsing_enums():
    row = {
        "Stock Number": "321",
        "Year": "2018",
        "Make": "BMW",
        "Model": "X5",
        "Vin#": "VINBMW",
        "Fuel Type": "Gasoline",
        "Seller Type": "Insurance",
    }

    vehicle = VehicleFactory.from_csv_row(row)

    assert vehicle.fuel_type.value == "Gasoline"
    assert vehicle.seller_type.value == "Insurance"


def test_parse_float_empty():
    assert VehicleFactory.parse_float("") is None
    assert VehicleFactory.parse_float(None) is None


def test_parse_int_empty():
    assert VehicleFactory.parse_int("") is None
    assert VehicleFactory.parse_int(None) is None
