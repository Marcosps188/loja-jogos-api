from database import SessionLocal, engine, Base
from models import Categoria, Plataforma


Base.metadata.create_all(bind=engine)

db = SessionLocal()


categorias = [
    "Ação",
    "Aventura",
    "RPG",
    "Esportes",
    "Corrida",
    "Estratégia",
    "Terror",
    "Simulação",
]


plataformas = [
    "PC",
    "PlayStation 5",
    "PlayStation 4",
    "Xbox Series X/S",
    "Xbox One",
    "Nintendo Switch",
]


for nome in categorias:
    existente = db.query(Categoria).filter(Categoria.nome == nome).first()

    if not existente:
        db.add(Categoria(nome=nome))


for nome in plataformas:
    existente = db.query(Plataforma).filter(Plataforma.nome == nome).first()

    if not existente:
        db.add(Plataforma(nome=nome))


db.commit()

db.close()

print("Categorias e plataformas cadastradas com sucesso!")