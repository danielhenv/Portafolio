import json
import os
from typing import List, Optional
from domain import Reservation

class ReservationRepository:
    def __init__(self, filename: str = "reservas.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump([], f)

    def _load(self) -> List[Reservation]:
        with open(self.filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [Reservation(**r) for r in data]

    def _save(self, reservas: List[Reservation]):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([r.to_dict() for r in reservas], f, indent=4, ensure_ascii=False)

    def add(self, res: Reservation) -> Reservation:
        reservas = self._load()
        reservas.append(res)
        self._save(reservas)
        return res

    def list_all(self) -> List[Reservation]:
        return self._load()

    def get(self, rid: str) -> Optional[Reservation]:
        return next((r for r in self._load() if r.id == rid), None)

    def update(self, updated: Reservation) -> Optional[Reservation]:
        reservas = self._load()
        for i, r in enumerate(reservas):
            if r.id == updated.id:
                reservas[i] = updated
                self._save(reservas)
                return updated
        return None

    def delete(self, rid: str) -> bool:
        reservas = self._load()
        nuevas = [r for r in reservas if r.id != rid]
        if len(nuevas) != len(reservas):
            self._save(nuevas)
            return True
        return False