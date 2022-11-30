from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from databases import Database
from schema import UserSchema
from config import DB_URL

print(DB_URL)
print('Init...')
database = Database(DB_URL)
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    dad = Column(String(50))
    phone = Column(String(50))
    text = Column(String(500))

    @staticmethod
    async def add_user(data: UserSchema):
        query = User.__table__.insert().values(**data.dict())
        await database.execute(query)
