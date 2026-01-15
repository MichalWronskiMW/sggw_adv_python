import csv
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from .factory import VehicleFactory, AuctionFactory


def load_single_csv(csv_file: Path) -> list:
    auctions = []
    with open(csv_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            vehicle = VehicleFactory.from_csv_row(row)
            auction = AuctionFactory.from_csv_row(row, vehicle)
            auctions.append(auction)
    return auctions


def load_all_csvs(data_path: str) -> list:
    data_path = Path(data_path)
    csv_files = list(data_path.glob("*.csv"))

    if not csv_files:
        print(f"No CSV files found in: {data_path}")
        return []

    auctions = []

    # 👇 MULTITHREADING
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(load_single_csv, csv_file) for csv_file in csv_files]

        for future in as_completed(futures):
            auctions.extend(future.result())

    print(f"Loaded auctions (multithreaded): {len(auctions)}")
    return auctions
