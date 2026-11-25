from litestar import Router

from .users import UserController

__all__ = ["api_router"]

api_router = Router(
    path="/api",
    route_handlers=[UserController],
)
