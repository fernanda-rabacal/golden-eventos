from pydantic import BaseModel
from api.core.models.exceptions import UsuarioException


class UserDTO(BaseModel):
    id: int | None = None
    nome: str | None = None
    email: str | None = None
    cpf: str | None = None
    promotor: bool | None = None


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
    
    def edit_validations(self) -> None:
        if self.id is None:
            raise UsuarioException (
                'CAMPO_OBRIGATORIO', 
                f'O campo id é obrigatório e não pode ser nulo.'
            )
        
        if str(self.id).strip() == '':
            raise UsuarioException (
               'CAMPO_OBRIGATORIO', 
                f'O campo id é obrigatório e não pode ser vazio.'
            )
    
    def create_validations(self) -> UsuarioException | None:
        ''' Validações para criar usuario '''
        self.id = None  
        fields = ['nome', 'email', 'senha', 'cpf']
        for field in fields:
            if self.__dict__[field] is None:
                raise UsuarioException (
                    'CAMPO_OBRIGATORIO', 
                    f'O campo {field} é obrigatório e não pode ser nulo.'
                )

            if self.__dict__[field].strip() == '':
                raise UsuarioException (
                    'CAMPO_OBRIGATORIO', 
                    f'O campo {field} é obrigatório e não pode ser vazio.'
                )
        
        if len(self.senha) < 6:
            raise UsuarioException (
                'VALIDATION_ERROR',
                'A senha deve ter pelo menos 6 caracteres.'
            )
        
        if len(self.cpf) < 11 or len(self.cpf) > 11:
            raise UsuarioException (
                'VALIDATION_ERROR',
                'O cpf está com o tamanho invalido.'
            )
