import uvicorn
from app import create_app, FastAPI
from database.schemas import create_tables


golden_app: FastAPI = create_app(
    title='api-gondel-eventos', 
    description='Uma api de um site de gerenciamento de eventos'
)


if __name__ == "__main__":
    create_tables()
    uvicorn.run (
        app = 'main:golden_app',
        host = '0.0.0.0',
        port = 8001,
        reload = True
    )