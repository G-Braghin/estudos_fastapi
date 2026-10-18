from dataclasses import asdict

from sqlalchemy import select

from estudo_fastapi.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='Bob', email='bob@examplo.com', password='password'
        )
        session.add(new_user)
        session.commit()

        user = session.scalar(select(User).where(User.username == 'Bob'))
        assert asdict(user) == {
            'id': 1,
            'username': 'Bob',
            'email': 'bob@examplo.com',
            'password': 'password',
            'created_at': time,
            'updated_at': time,
        }
