import uuid
from typing import List, Optional
from domain import Reservation
from storage import ReservationRepository
from validators import (
    is_valid_email, is_valid_phone, is_valid_date, is_valid_time
)
from colorama import Fore, Style

class ReservationService:
    def __init__(self, repo: Optional[ReservationRepository] = None):
        self.repo = repo or ReservationRepository()

    # --- CRUD ---
    def create(self, **data) -> Reservation:
        self._validate_data(data)
        if self._is_overlapping(data["date"], data["time"]):
            print(Fore.RED + "⚠ Ya existe una reserva en esa fecha y hora." + Style.RESET_ALL)
            return None
        rid = str(uuid.uuid4())
        res = Reservation(id=rid, **data)
        created = self.repo.add(res)
        print(Fore.GREEN + "✅ Reserva creada con éxito." + Style.RESET_ALL)
        return created

    def list_all(self) -> List[Reservation]:
        return self.repo.list_all()

    def get(self, rid: str) -> Optional[Reservation]:
        return self.repo.get(rid)

    def update(self, rid: str, **data) -> Optional[Reservation]:
        current = self.repo.get(rid)
        if not current:
            print(Fore.RED + "⚠ No se encontró la reserva a modificar." + Style.RESET_ALL)
            return None
        merged = {**current.to_dict(), **data, "id": rid}
        self._validate_data(merged)
        if self._is_overlapping(merged["date"], merged["time"], exclude_id=rid):
            print(Fore.RED + "⚠ Ya existe otra reserva en esa fecha y hora." + Style.RESET_ALL)
            return None
        updated = Reservation(**merged)
        self.repo.update(updated)
        print(Fore.GREEN + "✅ Reserva modificada con éxito." + Style.RESET_ALL)
        return updated

    def delete(self, rid: str) -> bool:
        deleted = self.repo.delete(rid)
        if deleted:
            print(Fore.GREEN + "🗑 Reserva eliminada con éxito." + Style.RESET_ALL)
        else:
            print(Fore.RED + "⚠ No se encontró la reserva a eliminar." + Style.RESET_ALL)
        return deleted

    # --- Búsquedas ---
    def search_by_customer(self, name_part: str) -> List[Reservation]:
        name_part = name_part.lower().strip()
        return [r for r in self.repo.list_all() if name_part in r.customer_name.lower()]

    def search_by_date(self, date: str) -> List[Reservation]:
        if not is_valid_date(date):
            print(Fore.RED + "⚠ Fecha inválida." + Style.RESET_ALL)
            return []
        return [r for r in self.repo.list_all() if r.date == date]

    # --- Utilidades ---
    def format_reservation(self, r: Reservation) -> str:
        return (
            f"ID: {r.id}\n"
            f"Cliente: {r.customer_name}\n"
            f"Email/Teléfono: {r.email} / {r.phone}\n"
            f"Recogida: {r.pickup_address}\n"
            f"Entrega: {r.delivery_address}\n"
            f"Fecha/Hora: {r.date} {r.time}\n"
            f"Servicio: {r.service_type}\n"
            f"Notas: {r.notes or '-'}"
        )

    def _validate_data(self, d: dict):
        if not d.get("customer_name"):
            raise ValueError("El nombre del cliente es obligatorio.")
        if not is_valid_email(d.get("email", "")):
            raise ValueError("El email no es válido.")
        if not is_valid_phone(d.get("phone", "")):
            raise ValueError("El teléfono no es válido.")
        if not is_valid_date(d.get("date", "")):
            raise ValueError("La fecha no es válida (formato AAAA-MM-DD).")
        if not is_valid_time(d.get("time", "")):
            raise ValueError("La hora no es válida (formato HH:MM).")

    def _is_overlapping(self, date: str, time: str, exclude_id: Optional[str] = None) -> bool:
        for r in self.repo.list_all():
            if exclude_id and r.id == exclude_id:
                continue
            if r.date == date and r.time == time:
                return True
        return False