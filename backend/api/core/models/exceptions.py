class BaseException(Exception):
    ''' Exceção base '''
    def __init__(self, status, message) -> None:
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
    pass

class UsuarioException(CoreException):
    ''' Exceção relacionada as validações de usuario '''
    pass

class DatabaseException(BaseException):
    ''' Exceção relacionada a problemas com o banco de dados '''
    def __init__(self, status, message, error) -> None:
        self.error = error
        super().__init__(status, message)
        