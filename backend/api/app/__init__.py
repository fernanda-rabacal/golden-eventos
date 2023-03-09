'''
Camada Application da aplicação

Aqui onde acontece o gerenciamento dos endpoints
'''
from fastapi import FastAPI


def create_app(title: str, description: str) -> FastAPI:
    '''
    função para criar a aplicação principal
    '''
    import api.app.commands.user_controller as users


    app = FastAPI (
        title=title, 
        description=description
    )

    app.include_router(users.router)
    return app
