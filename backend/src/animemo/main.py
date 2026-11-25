import uvicorn
from litestar import Litestar

from animemo.api import api_router
from animemo.config import Config


def main() -> None:
    config = Config()

    app = Litestar(route_handlers=[api_router])

    uvicorn.run(
        app=app,
        host=config.server.host,
        port=config.server.port,
    )


if __name__ == "__main__":
    main()
