from src.factory import VehicleFactory


def test_vehicle_parsing():
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

    assert vehicle.year == 2020
    assert vehicle.current_bid == 10500.0
    assert vehicle.odometer == 100000
