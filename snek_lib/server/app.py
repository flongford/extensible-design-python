import importlib.metadata
import os
from typing import Optional
from dataclasses import asdict

from fastapi import FastAPI, Depends

from snek_lib.core.i_snek_repository import ISnekRepository
from snek_lib.utilities import load_snek_repository_factory


def create_app() -> FastAPI:
    """
    Entry point for faskapi / uvicorn.

    Start uvicorn with (for example):

        uvicorn --factory snek_lib.server.app:create_app

    This function returns a ASGI app.
    """
    app = FastAPI(
        title="Snek API",
        version=importlib.metadata.version("snek_lib"),
    )
    snek_repository_factory = load_snek_repository_factory(
        factory_name=os.getenv("SNEK_REPOSITORY_FACTORY_NAME", "fake")
    )

    @app.get("/sneks")
    def get_sneks(
        name: Optional[str] = None,
        snek_repository: ISnekRepository = Depends(
            snek_repository_factory
        )
    ):
        sneks = {}
        for snek_id in snek_repository.list_sneks():
            snek = snek_repository.get_snek(snek_id)
            if name is None or name == snek.name:
                sneks[snek_id] = asdict(snek)
        return {
            "sneks": sneks
        }

    return app
