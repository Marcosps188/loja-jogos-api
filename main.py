
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from database import Base, engine
from routers import jogos
from routers import plataformas
from routers import categorias


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Level Games",
    description="API para gerenciamento de jogos de uma loja.",
    version="3.0.0"
)


@app.exception_handler(RequestValidationError)
async def tratar_erros_validacao(
    request: Request,
    exc: RequestValidationError
):
    erros = []

    for erro in exc.errors():
        campo = erro["loc"][-1]
        mensagem = erro["msg"]

        if erro["type"] == "missing":
            mensagem = f"O campo '{campo}' é obrigatório."

        else:
            if mensagem.startswith("Value error, "):
                mensagem = mensagem.replace("Value error, ", "", 1)

            if campo == "body":
                mensagem_original = str(
                    erro.get("ctx", {}).get("error", "")
                ).lower()

                if "nome" in mensagem_original:
                    campo = "nome"
                elif "usuario" in mensagem_original or "usuário" in mensagem_original:
                    campo = "usuario"

        erros.append({
            "campo": campo,
            "mensagem": mensagem
        })

    return JSONResponse(
        status_code=422,
        content={"detail": erros}
    )


app.include_router(jogos.router)
app.include_router(plataformas.router)
app.include_router(categorias.router)


@app.get("/")
def raiz():
    return {
        "status": "API da Loja de Jogos funcionando!"
    }
