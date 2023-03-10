from http import HTTPStatus


class BaseException(Exception):
    ''' Exceção base '''
    def __init__(self, status: str, message: str) -> None:
        self.status = status
        self.message = message

class NotFoundException(BaseException):
    ''' Exceção para quando o recurso não é encontrado '''
    pass

class NoContentException(Exception):
    ''' Exceção quando o recurso é encontrado, mas não há conteudo (listas vazias por exemplo) '''
    pass

class CoreException(BaseException):
    ''' Exceção generica relacionada as regras de negocio e validações '''
    def __init__(self, status: str, message: str, status_code: int = HTTPStatus.BAD_REQUEST) -> None:
        self.status_code = status_code
        super().__init__(status, message)

class UsuarioException(CoreException):
    ''' Exceção relacionada as validações de usuario '''
    pass

class DatabaseException(BaseException):
    ''' Exceção relacionada a problemas com o banco de dados '''
    def __init__(self, status: str, message: str, error: str) -> None:
        self.error = error
        super().__init__(status, message)

class AuthException(BaseException):
    pass