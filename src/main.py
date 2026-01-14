from pathlib import Path
from .csv_parser import load_all_csvs

def main():
    data_path = Path(__file__).parent.parent / "data" / "raw"
    auctions = load_all_csvs(data_path)

    if not auctions:
        print("No auctions loaded. Check CSV files and format.")
        return

    total_vehicles = sum(len(a.vehicles) for a in auctions)
    avg_year = sum(v.year for a in auctions for v in a.vehicles if v.year) / total_vehicles
    print(f"Total auctions: {len(auctions)}, Total vehicles: {total_vehicles}")
    print(f"Average vehicle year: {avg_year:.2f}")

if __name__ == "__main__":
    main()
