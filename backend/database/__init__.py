from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session


DBMS: str = 'MYSQL'
DATABASE: str = 'golden_eventos'

match DBMS:
    case 'MYSQL':
        conx_str = f'mysql+mysqlconnector://root@localhost:3306/{DATABASE}'
    case 'SQLITE':
        conx_str = rf'sqlite:///database\{DATABASE}.db'

engine: Engine = create_engine(conx_str)


def session_factory() -> Session:
    session: Session = sessionmaker(bind=engine)
    return session()
    