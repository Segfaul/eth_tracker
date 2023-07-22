from app.models.models import User
from app.logs import logger, log


class UserService:

    def __init__(self) -> None:
        ...

    #  --------------------User Logic--------------------
    @classmethod
    @log(logger)
    async def get_user(cls, tg_id: int) -> dict or int:
        user_obj = await User.filter(id=tg_id).first().values()
        return user_obj

    @classmethod
    @log(logger)
    async def add_user(cls, tg_id: int, username: str = None, is_admin: bool = False):
        user_obj = await User.filter(id=tg_id).first()

        if not user_obj:
            await User.create(id=tg_id, username=username, is_admin=is_admin)
            return 0
        
        else:
            user_obj.username = username
            await user_obj.save()
            return 1

    @classmethod
    @log(logger)
    async def update_notification(cls, tg_id: int):
        user_obj = await User.filter(id=tg_id).first()

        if user_obj:
            user_obj.notification = 0 if user_obj.notification else 1
            await user_obj.save()
            return user_obj.notification

    @classmethod
    @log(logger)
    async def update_percent(cls, tg_id: int, percent: float):
        user_obj = await User.filter(id=tg_id).first()

        if user_obj:
            user_obj.percent = percent
            await user_obj.save()
            return 0

    #  --------------------Admin Logic--------------------
    @classmethod
    @property
    @log(logger)
    async def get_admins(cls):
        admin_objs = await User.filter(is_admin=True).values('id')

        if admin_objs:
            return admin_objs
    
    @classmethod
    @property
    @log(logger)
    async def get_ready_users(cls):
        user_objs = await User.filter(notification=True).values('id', 'percent')

        if user_objs:
            return user_objs

    @classmethod
    @log(logger)
    async def update_admin(cls, tg_id: int, status: int):
        user_obj = await User.filter(id=tg_id).first()

        if user_obj:
            user_obj.is_admin = status
            await user_obj.save()
            return 0
