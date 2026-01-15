import csv
from pathlib import Path
from .csv_parser import load_all_csvs


def save_vehicles_csv(auctions, filename="data/processed/vehicles_out.csv"):
    output_path = Path(filename)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Stock Number", "Year", "Make", "Model", "VIN",
            "Current Bid", "Odometer", "Fuel Type", "Seller Type"
        ])

        for auction in auctions:
            for vehicle in auction.vehicles:
                writer.writerow([
                    vehicle.stock_number,
                    vehicle.year,
                    vehicle.make,
                    vehicle.model,
                    vehicle.vin,
                    vehicle.current_bid,
                    vehicle.odometer,
                    vehicle.fuel_type.value if vehicle.fuel_type else None,
                    vehicle.seller_type.value if vehicle.seller_type else None,
                ])

    print(f"Saved vehicles to {output_path}")


def main():
    data_path = Path(__file__).parent.parent / "data" / "raw"
    auctions = load_all_csvs(data_path)

    if not auctions:
        print("No auctions loaded. Check CSV files and format.")
        return

    total_vehicles = sum(len(a.vehicles) for a in auctions)
    avg_year = (
        sum(v.year for a in auctions for v in a.vehicles if v.year)
        / total_vehicles
    )

    print(f"Total auctions: {len(auctions)}, Total vehicles: {total_vehicles}")
    print(f"Average vehicle year: {avg_year:.2f}")

    # <<< TO JEST KLUCZOWE >>>
    save_vehicles_csv(auctions)


if __name__ == "__main__":
    main()
