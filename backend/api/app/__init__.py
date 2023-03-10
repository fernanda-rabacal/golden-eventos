'''
Camada Application da aplicação

Aqui onde acontece o gerenciamento dos endpoints e handlers
'''
from fastapi import FastAPI
from api.core.models.exceptions import (
    CoreException, DatabaseException, NotFoundException, NoContentException
)


def add_routers(app: FastAPI) -> FastAPI:
    '''
    Adiciona as rotas das aplicação
    '''
    import api.app.commands.user_controller as user


    app.include_router(user.router)
    return app

def add_exception_handlers(app: FastAPI) -> FastAPI:
    ''' Adiciona os Exceptions Handlers a aplicação '''
    import api.app.errors.handlers as handlers


    app.add_exception_handler(CoreException, handlers.core_exception_handler)
    app.add_exception_handler(DatabaseException, handlers.database_exception_handler)
    app.add_exception_handler(NotFoundException, handlers.not_found_exception_handler)
    app.add_exception_handler(NoContentException, handlers.no_content_exception_handler)
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
