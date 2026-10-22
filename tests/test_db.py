from dataclasses import asdict

import pytest
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from estudo_fastapi.models import User


@pytest.mark.asyncio
async def test_create_user(session: AsyncSession, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='Bob', email='bob@examplo.com', password='password'
        )
        session.add(new_user)
        await session.commit()

        user = await session.scalar(select(User).where(User.username == 'Bob'))
        assert asdict(user) == {
            'id': 1,
            'username': 'Bob',
            'email': 'bob@examplo.com',
            'password': 'password',
            'created_at': time,
            'updated_at': time,
        }
