from datetime import datetime
from typing import Dict, Optional
from .models import Vehicle, Auction
from .enums import FuelType, SellerType

class VehicleFactory:

    @staticmethod
    def parse_float(value: str) -> Optional[float]:
        if not value or value.strip() == "":
            return None
        try:
            return float(value.replace("$", "").replace("USD", "").replace(",", "").strip())
        except ValueError:
            return None

    @staticmethod
    def parse_int(value: str) -> Optional[int]:
        if not value or value.strip() == "":
            return None
        try:
            return int(value.replace(",", "").replace(" mi", "").strip())
        except ValueError:
            return None

    @staticmethod
    def from_csv_row(row: Dict[str, str]) -> Vehicle:
        def get_val(key: str) -> Optional[str]:
            val = row.get(key)
            return val.strip() if val else None

        return Vehicle(
            stock_number=get_val("Stock Number"),
            year=int(get_val("Year")) if get_val("Year") else None,
            make=get_val("Make"),
            model=get_val("Model"),
            vin=get_val("Vin#"),
            current_bid=VehicleFactory.parse_float(get_val("Current Bid") or ""),
            odometer=VehicleFactory.parse_int(get_val("Odometer") or ""),
            fuel_type=FuelType(get_val("Fuel Type")) if get_val("Fuel Type") else None,
            seller_type=SellerType(get_val("Seller Type")) if get_val("Seller Type") else None,
            transmission=get_val("Transmission Type"),
            drive_line=get_val("Drive Line Type"),
            body_style=get_val("Body Style"),
            primary_damage=get_val("Primary Damage"),
            secondary_damage=get_val("Secondary Damage"),
        )


class AuctionFactory:

    @staticmethod
    def parse_date(date_str: str) -> Optional[datetime]:
        if not date_str:
            return None
        date_str = date_str.strip()
        formats = ["%a %b %d, %I:%M%p %Z", "%a %b %d, %I:%M%p"]  # obsługa CST/CDT i bez strefy
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        return None

    @staticmethod
    def from_csv_row(row: Dict[str, str], vehicle: Vehicle) -> Auction:
        def get_val(key: str) -> Optional[str]:
            val = row.get(key)
            return val.strip() if val else None

        auction_date = AuctionFactory.parse_date(get_val("Auction Date"))
        timed_auction_val = get_val("Timed Auction")
        timed_auction = (timed_auction_val.upper() == "YES") if timed_auction_val else False

        return Auction(
            auction_date=auction_date,
            branch_name=get_val("Branch Name"),
            timed_auction=timed_auction,
            vehicles=[vehicle],
        )
