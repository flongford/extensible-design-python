from dataclasses import dataclass


@dataclass(frozen=True)
class Snek:
    """Main product of Snek Semiconductors and Software, Incorporated."""

    # Human-readable name of this snek
    name: str

    # Unique content of this snek
    content: str
