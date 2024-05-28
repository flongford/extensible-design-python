import argparse
from typing import Generator

from snek_lib.core.i_snek_repository import ISnekRepository
from snek_lib.model.snek import Snek
from snek_lib.utilities import load_snek_repository_factory

SNEK_REPOSITORY_BACKEND = "fake"


def load_all_sneks(
    snek_repository: ISnekRepository
) -> Generator[Snek, None, None]:
    """Return all sneks registered in a given snek repository"""
    for snek_id in snek_repository.list_sneks():
        yield snek_repository.get_snek(snek_id)


def main():
    parser = argparse.ArgumentParser(prog=__name__)
    parser.add_argument(
        "--type",
        type=str,
        dest="snek_id",
        help="Snek to load",
    )

    args = parser.parse_args()

    snek_repository = load_snek_repository_factory(SNEK_REPOSITORY_BACKEND)()
    if args.snek_id is None:
        for snek in load_all_sneks(snek_repository):
            print(f"{snek.name}:\n{snek.content}")
    else:
        snek = snek_repository.get_snek(args.snek_id)
        print(f"{snek.name}:\n{snek.content}")


if __name__ == '__main__':
    main()
