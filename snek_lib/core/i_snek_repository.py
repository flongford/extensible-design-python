from abc import abstractmethod, ABC
from typing import Callable, List

from snek_lib.model.snek import Snek
from snek_lib.model.snek_id import SnekID


class ISnekRepository(ABC):
    """Generic API for a repository service handling sneks"""

    @abstractmethod
    def list_sneks(self) -> List[SnekID]:
        """Return a list of snek IDs corresponding to each snek registered
        with the data store"""

    @abstractmethod
    def put_snek(self, snek_id: SnekID, snek: Snek) -> None:
        """Add or update snek with corresponding ID in data store"""

    @abstractmethod
    def get_snek(self, snek_id: SnekID) -> Snek:
        """Return snek with corresponding ID from data store"""

    @abstractmethod
    def delete_snek(self, snek_id: SnekID) -> Snek:
        """Remove snek with corresponding ID from data store"""


# Zero-argument callable that instantiates a concrete implementation of
# ISnekRepository
ISnekRepositoryFactory = Callable[[], ISnekRepository]
