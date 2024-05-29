import importlib.metadata
from typing import Dict, Optional

from snek_lib.core.i_snek_repository import ISnekRepositoryFactory
from snek_lib.model.snek import Snek
from snek_lib.model.snek_id import SnekID

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


def bootstrap_sneks() -> Dict[SnekID, Snek]:
    """Return set of (SnekID, Snek) key, value pairs that should
    be shipped with every snek server deployment.
    """
    return {
        SnekID("normal"): Snek(
            name="normal",
            content="""\
                        --..,_                     _,.--.
                           `'.'.                .'`__ o  `;__.
                              '.'.            .'.'`  '---'`  `
                                '.`'--....--'`.'
                                  `'--....--'`
                    """
        ),
        SnekID("fancy"): Snek(
            name="fancy",
            content="""\
                                              _,..,,,_
                                         '``````^~"-,_`"-,_
                           .-~c~-.                    `~:. ^-.
                       `~~~-.c    ;                      `:.  `-,     _.-~~^^~:.
                             `.   ;      _,--~~~~-._       `:.   ~. .~          `.
                              .` ;'   .:`           `:       `:.   `    _.:-,.    `.
                            .' .:   :'    _.-~^~-.    `.       `..'   .:      `.    '
                           :  .' _:'   .-'        `.    :.     .:   .'`.        :    ;
                           :  `-'   .:'             `.    `^~~^`   .:.  `.      ;    ;
                            `-.__,-~                  ~-.        ,' ':    '.__.`    :'
                                                         ~--..--'     ':.         .:'
                                                                         ':..___.:'
                    """
        ),
        SnekID("cute"): Snek(
            name="cute",
            content=r"""
                                /^\/^\
                              _|__|  O|
                        \/     /~     \_/ \
                        \____|__________/  \
                             \_______      \
                                     `\     \                 \
                                       |     |                  \
                                      /      /                    \
                                     /     /                       \
                                   /      /                         \ \
                                  /     /                            \  \
                                /     /             _----_            \   \
                               /     /           _-~      ~-_         |   |
                              (      (        _-~    _--_    ~-_     _/   |
                               \      ~-____-~    _-~    ~-_    ~-_-~    /
                                 ~-_           _-~          ~-_       _-~ 
                                    ~--______-~                ~-___-~
                    """
        ),
    }
