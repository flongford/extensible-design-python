from typing import List

from snek_lib.core.i_snek_repository import ISnekRepository
from snek_lib.model.snek import Snek
from snek_lib.model.snek_id import SnekID


class FakeSnekRepository(ISnekRepository):

    def __init__(self):
        self._store = {
            SnekID("normal"): Snek(
                name="Normal",
                content="""\
                    --..,_                     _,.--.
                       `'.'.                .'`__ o  `;__.
                          '.'.            .'.'`  '---'`  `
                            '.`'--....--'`.'
                              `'--....--'`
                """
            ),
            SnekID("fancy"): Snek(
                name="Fancy",
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
                name="Cute",
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
