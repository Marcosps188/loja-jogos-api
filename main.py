from fastapi import FastAPI

app = FastAPI(
    title="Loja de Jogos API",
    description="API para gerenciamento de jogos de uma loja.",
    version="1.0.0"
)

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
def listar_jogos():
    return jogos
