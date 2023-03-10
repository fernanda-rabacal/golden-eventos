'''
Camada Application

Aqui onde acontece o gerenciamento dos endpoints e handlers
'''
from fastapi import FastAPI
from app.errors.exceptions import (
    AuthException, CoreException, DatabaseException, NotFoundException, NoContentException
)


def add_routers(app: FastAPI) -> FastAPI:
    '''
    Adiciona as rotas das aplicação
    '''
    import app.commands.user_controller as user


    app.include_router(user.router)
    return app

def add_exception_handlers(app: FastAPI) -> FastAPI:
    ''' Adiciona os Exceptions Handlers a aplicação '''
    import app.errors.exception_handlers as error


    app.add_exception_handler(CoreException, error.core_exception_handler)
    app.add_exception_handler(DatabaseException, error.database_exception_handler)
    app.add_exception_handler(NotFoundException, error.not_found_exception_handler)
    app.add_exception_handler(NoContentException, error.no_content_exception_handler)
    app.add_exception_handler(AuthException, error.auth_exception_handler)
    return app

def create_app(title: str, description: str) -> FastAPI:
    '''
    Função para instânciar a aplicação principal

    params
    ------
    title : str
        titulo da aplicação
    description : str
        descrição da aplicação
    '''
    
    app = FastAPI (
        title=title, 
        description=description
    )

    app = add_routers(app)
    app = add_exception_handlers(app)
    return app
