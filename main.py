from fastapi import FastAPI

from database import Base, engine
from routers import jogos
from routers import plataformas
from routers import categorias


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Loja de Jogos API",
    description="API para gerenciamento de jogos de uma loja.",
    version="3.0.0"
)


app.include_router(jogos.router)
app.include_router(plataformas.router)
app.include_router(categorias.router)


@app.get("/")
def raiz():
    return {
        "status": "API da Loja de Jogos funcionando!"
    }