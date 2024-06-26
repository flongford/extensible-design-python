import argparse
from typing import Generator, Optional

import httpx

from snek_lib.model.snek import Snek


def download_sneks(
    snek_host_url: str,
    name: Optional[str] = None
) -> Generator[Snek, None, None]:
    """Return all sneks registered in a given snek repository, optionally
    filtering by name.
    """
    url = snek_host_url + "/sneks"
    if name:
        url += f"?name={name}"
    response = httpx.get(url)
    response.raise_for_status()
    for snek_data in response.json()["sneks"].values():
        yield Snek(**snek_data)


def main():
    parser = argparse.ArgumentParser(prog=__name__)
    parser.add_argument(
        "--type",
        type=str,
        dest="snek_name",
        help="Snek to load",
    )
    parser.add_argument(
        "--snek-host-url",
        type=str,
        help="Host for Snek API",
        default="http://localhost:8000"
    )
    args = parser.parse_args()

    for snek in download_sneks(
        args.snek_host_url,
        name=args.snek_name
    ):
        print(snek)


if __name__ == '__main__':
    main()
