from nest.core import Controller, Get, Post, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.config import config

from .user_service import UserService
from .user_model import User


@Controller("users")
class UserController:
    def __init__(self, user_service: UserService):  # type: ignore
        self.user_service = user_service

    @Get("/")
    async def get_users(self, session: AsyncSession = Depends(config.get_db)):
        return await self.user_service.get_users(session)

    @Post("/")
    async def add_user(
        self, user: User, session: AsyncSession = Depends(config.get_db)
    ):
        return await self.user_service.add_user(user, session)
