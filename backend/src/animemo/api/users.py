from litestar import Controller, get

from animemo.schemas import User


class UserController(Controller):
    path = "/users"

    @get("/")
    async def list_users(self) -> list[User]:
        # TEST: test data
        return [User(id=0, username="Luffy")]
