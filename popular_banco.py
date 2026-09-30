from database import SessionLocal
from models import Plataforma, Categoria


db = SessionLocal()

try:

    
    plataformas = [
        "PC",
        "PlayStation 5",
        "PlayStation 4",
        "Xbox Series X/S",
        "Xbox One",
        "Nintendo Switch"
    ]

    for nome in plataformas:

        existe = db.query(Plataforma).filter(
            Plataforma.nome == nome
        ).first()

        if not existe:
            db.add(Plataforma(nome=nome))


   
    categorias = [
        "Ação",
        "Aventura",
        "RPG",
        "Esportes",
        "Corrida",
        "Estratégia",
        "Terror",
        "Simulação"
    ]

    for nome in categorias:

        existe = db.query(Categoria).filter(
            Categoria.nome == nome
        ).first()

        if not existe:
            db.add(Categoria(nome=nome))


    db.commit()

    print("Plataformas e categorias cadastradas com sucesso!")


finally:
    db.close()