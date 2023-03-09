from database.connection import engine
from sqlalchemy.orm import relationship, declarative_base, DeclarativeBase
from sqlalchemy import Column, Integer, Boolean, String, DateTime
from core.models.user import UserDO


Model: DeclarativeBase = declarative_base()


if __name__ != '__main__':
    Model.metadata.create_all(bind=engine)