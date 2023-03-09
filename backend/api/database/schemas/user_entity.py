from api.database.schemas import *


class UserEntity(Model):
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    email: str = Column(String(255), nullable=False, unique=True) 
    senha: str = Column(String(255), nullable=False)
    nome: str = Column(String(255), nullable=False)
    cpf: str = Column(String(12), nullable=False)
    promotor: bool = Column(Boolean, nullable=False)

    def __init__(self, id: int, email: str, senha: str , nome: str, cpf: str, promotor: bool) -> None:
        self.id = id
        self.email = email
        self.senha = senha
        self.nome = nome
        self.cpf = cpf
        self.promotor = promotor
    
    def __str__(self) -> str:
        return f'<{self.username}>'