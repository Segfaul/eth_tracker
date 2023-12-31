from tortoise import Tortoise

from app.services.user_service import UserService
from app.logs import logger, log


class DatabaseService:

    def __init__(self, debug: bool = True,
                 postgre_con: str = "postgres://postgres:pass@db.host:5432/somedb", 
                 admins: list = None) -> None:
        
        self.db_url = "sqlite://db.sqlite3" if debug else postgre_con
        self.admins = admins

    @log(logger)
    async def init_db(self) -> None:
        await Tortoise.init(
            db_url=self.db_url,
            modules={"models": ["app.models.models"]},
            timezone='Europe/Moscow'
        )
        await Tortoise.generate_schemas()

        if self.admins:
            for admin_id in self.admins:
                await UserService.add_user(tg_id=admin_id, is_admin=True)

    @classmethod
    @log(logger)
    async def close_db(cls) -> None:
        await Tortoise.close_connections()
