from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session


# engine = create_engine('mysql+mysqlconnector://root@localhost:3306/livraria')
engine: Engine = create_engine(r'sqlite:///database\autorizacao.db')


def session_factory() -> Session:
    session: Session = sessionmaker(bind=engine)
    return session()
