import json
import os
from pathlib import Path
from dataclasses import asdict
from typing import Any, Dict, List

from snek_lib.core.i_snek_repository import ISnekRepository
from snek_lib.model.snek import Snek
from snek_lib.model.snek_id import SnekID


class LocalSnekRepository(ISnekRepository):

    def __init__(self, root: Path):
        self._root = root

    def _get_snek_store(self) -> Dict[SnekID, Any]:
        """Loads and returns a copy of the snek store from a
        JSON file.
        """
        return (
            json.loads(self._root.read_text(encoding="utf-8"))
            if self._root.exists()
            else {}
        )

    def _put_job_store(self, data: Dict[SnekID, Any]):
        """Updates state of JSON file containing snek store.
        """
        self._root.write_text(json.dumps(data), encoding="utf-8")

    def list_sneks(self) -> List[SnekID]:
        """Return a list of snek IDs corresponding to each snek registered
        with the data store"""
        store = self._get_snek_store()
        return list(store.keys())

    def put_snek(self, snek_id: SnekID, snek: Snek) -> None:
        """Add or update snek with corresponding ID in data store"""
        store = self._get_snek_store()
        store[snek_id] = asdict(snek)
        self._put_job_store(store)

    def get_snek(self, snek_id: SnekID) -> Snek:
        """Return snek with corresponding ID from data store"""
        data = self._get_snek_store()[snek_id]
        return Snek(**data)

    def delete_snek(self, snek_id: SnekID) -> None:
        """Remove snek with corresponding ID from data store"""
        store = self._get_snek_store()
        store.pop(snek_id)
        self._put_job_store(store)


def local_snek_repository_factory() -> LocalSnekRepository:
    """ISnekRepositoryFactory implementation that extracts
    any configuration details from the local environment and returns
    a LocalSnekRepository instance when invoked.
    """
    return LocalSnekRepository(
        root=Path(os.getenv("LOCAL_SNEK_REPOSITORY_ROOT"))
    )
