from api.database import engine
from sqlalchemy.orm import relationship, declarative_base, DeclarativeBase
from sqlalchemy import Column, Integer, Boolean, String, DateTime
from api.core.models.user import UserDO


Model: DeclarativeBase = declarative_base()


def create_tables() -> None:
    ''' Criar as tabelas no banco de acordo com os modelos do sqlalchemy '''
    Model.metadata.create_all(bind=engine)
