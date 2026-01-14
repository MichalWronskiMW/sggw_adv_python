import csv
from pathlib import Path
from .factory import VehicleFactory, AuctionFactory

def load_all_csvs(data_path: str | Path) -> list:
    data_path = Path(data_path)
    if not data_path.exists():
        print(f"Data folder not found: {data_path}")
        return []

    auctions = []
    total_rows = 0
    skipped_rows = 0

    csv_files = list(data_path.glob("*.csv"))
    if not csv_files:
        print(f"No CSV files found in: {data_path}")
        return []

    for csv_file in csv_files:
        print(f"Processing file: {csv_file.name}")
        with open(csv_file, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                total_rows += 1
                try:
                    vehicle = VehicleFactory.from_csv_row(row)
                    auction = AuctionFactory.from_csv_row(row, vehicle)
                    auctions.append(auction)
                except Exception as e:
                    skipped_rows += 1
                    print(f"  Skipping row {total_rows} due to error: {e}")

    print(f"Finished loading CSVs. Total rows: {total_rows}, Skipped: {skipped_rows}, Auctions loaded: {len(auctions)}")
    return auctions
