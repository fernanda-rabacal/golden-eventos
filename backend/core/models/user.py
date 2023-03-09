from pydantic import BaseModel
import random
from string import ascii_lowercase, ascii_uppercase, punctuation, digits
        

all_characters = ascii_lowercase + ascii_uppercase + punctuation + digits


class UserDTO(BaseModel):
    id: int | None = None
    email: str
    nome: str
    cpf: str
    promotor: bool = False


class UserDO(UserDTO):
    senha: str | None = None

    def to_dto(self) -> UserDTO:
        return UserDTO (
            id = self.id, 
            email = self.email,
            nome = self.nome,
            cpf = self.cpf,
            promotor = self.promotor 
        )
    
    def generate_password(self, lenght: int) -> None:
        if self.senha is None:
            self.senha = ''.join(random.sample(all_characters, lenght))
    
    def validate_edit(self) -> bool:
        if self.id is None:
            return False
    
    def validate_create(self) -> bool:
        if self.senha is None:
            return False