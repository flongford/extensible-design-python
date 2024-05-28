from abc import abstractmethod, ABC

from snek_lib.model.snek import Snek
from snek_lib.model.snek_id import SnekID


class ISnekRepository(ABC):
    """Generic API for a repository service handling sneks"""

    @abstractmethod
    def put_snek(self, snek_id: SnekID, snek: Snek) -> None:
        """Add or update snek with corresponding ID in data store"""

    @abstractmethod
    def get_snek(self, snek_id: SnekID) -> str:
        """Return snek with corresponding ID from data store"""

    @abstractmethod
    def delete_snek(self, snek_id: SnekID) -> str:
        """Remove snek with corresponding ID from data store"""
