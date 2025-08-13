from dataclasses import dataclass, asdict

@dataclass
class Reservation:
    id: str
    customer_name: str
    email: str
    phone: str
    pickup_address: str
    delivery_address: str
    date: str  # formato: AAAA-MM-DD
    time: str  # formato: HH:MM
    service_type: str
    notes: str = ""

    def to_dict(self):
        return asdict(self)