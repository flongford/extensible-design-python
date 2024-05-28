import importlib.metadata
from typing import Optional

from snek_lib.i_snek_repository import ISnekRepositoryFactory

SNEK_REPOSITORY_GROUP = "snek_repository_factories"


def load_snek_repository_factory(
    factory_name: str
) -> Optional[ISnekRepositoryFactory]:
    """Attempts to load and return factory function registered with a
    setuptools entry point called "snek_repository_factories"
    with a name that matches the given `factory_name`.

    Returns None if no factory with the given ID is found.
    """
    (entry_point,) = importlib.metadata.entry_points(
        group=SNEK_REPOSITORY_GROUP, name=factory_name
    )
    if entry_point is not None:
        return entry_point.load()
