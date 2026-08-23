from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Loja de Jogos API",
    description="API para gerenciamento de jogos de uma loja.",
    version="2.0.0"
)


class JogoSchema(BaseModel):
    nome: str
    preco: float
    plataforma: str
    categoria_id: int


jogos = [
    {
        "id": 1,
        "nome": "The Legend of Zelda: Breath of the Wild",
        "preco": 299.90,
        "plataforma": "Nintendo Switch",
        "categoria_id": 1
    },
    {
        "id": 2,
        "nome": "God of War Ragnarök",
        "preco": 249.90,
        "plataforma": "PlayStation 5",
        "categoria_id": 2
    },
    {
        "id": 3,
        "nome": "Forza Horizon 5",
        "preco": 199.90,
        "plataforma": "Xbox Series X",
        "categoria_id": 3
    },
    {
        "id": 4,
        "nome": "Minecraft",
        "preco": 129.90,
        "plataforma": "PC",
        "categoria_id": 4
    },
    {
        "id": 5,
        "nome": "EA Sports FC 26",
        "preco": 349.90,
        "plataforma": "PlayStation 5",
        "categoria_id": 5
    }
]


@app.get("/")
def raiz():
    return {"status": "API da Loja de Jogos funcionando!"}


@app.get("/jogos")
def listar_jogos(nome: str | None = None):

    if nome:
        jogos_filtrados = [
            jogo for jogo in jogos
            if nome.lower() in jogo["nome"].lower()
        ]

        return jogos_filtrados

    return jogos


@app.get("/jogos/{id}")
def buscar_jogo(id: int):

    for jogo in jogos:
        if jogo["id"] == id:
            return jogo

    raise HTTPException(
        status_code=404,
        detail="Jogo não encontrado."
    )


@app.post("/jogos", status_code=201)
def cadastrar_jogo(jogo: JogoSchema):

    novo_id = max([jogo["id"] for jogo in jogos], default=0) + 1

    novo_jogo = {
        "id": novo_id,
        "nome": jogo.nome,
        "preco": jogo.preco,
        "plataforma": jogo.plataforma,
        "categoria_id": jogo.categoria_id
    }

    jogos.append(novo_jogo)

    return novo_jogo


@app.delete("/jogos/{id}")
def remover_jogo(id: int):

    for jogo in jogos:
        if jogo["id"] == id:
            jogos.remove(jogo)

            return {
                "mensagem": "Jogo removido com sucesso."
            }

    raise HTTPException(
        status_code=404,
        detail="Jogo não encontrado."
    )