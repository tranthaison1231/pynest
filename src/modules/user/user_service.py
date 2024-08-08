from .user_model import User
from .user_entity import User as UserEntity
from nest.core.decorators.database import async_db_request_handler
from nest.core import Injectable

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


@Injectable
class UserService:
    @async_db_request_handler
    async def add_user(self, user: User, session: AsyncSession):
        new_user = UserEntity(**user.dict())
        session.add(new_user)
        await session.commit()
        return new_user.id

    @async_db_request_handler
    async def get_users(self, session: AsyncSession):
        query = select(UserEntity)
        result = await session.execute(query)
        return result.scalars().all()
