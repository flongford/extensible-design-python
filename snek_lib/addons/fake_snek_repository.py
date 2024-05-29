from typing import List

from snek_lib.core.i_snek_repository import ISnekRepository
from snek_lib.model.snek import Snek
from snek_lib.model.snek_id import SnekID
from snek_lib.utilities import bootstrap_sneks


class FakeSnekRepository(ISnekRepository):

    def __init__(self):
        self._store = bootstrap_sneks()

    def list_sneks(self) -> List[SnekID]:
        """Return a list of snek IDs corresponding to each snek registered
        with the data store"""
        return list(self._store.keys())

    def put_snek(self, snek_id: SnekID, snek: Snek) -> None:
        """Add or update snek with corresponding ID in data store"""
        self._store[snek_id] = snek

    def get_snek(self, snek_id: SnekID) -> Snek:
        """Return snek with corresponding ID from data store"""
        return self._store[snek_id]

    def delete_snek(self, snek_id: SnekID) -> None:
        """Remove snek with corresponding ID from data store"""
        self._store.pop(snek_id)
