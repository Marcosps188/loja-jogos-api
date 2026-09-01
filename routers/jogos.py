from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Jogo
from schemas import JogoCreateSchema, JogoResponseSchema


router = APIRouter(
    prefix="/jogos",
    tags=["Jogos"]
)


@router.get(
    "/",
    response_model=list[JogoResponseSchema]
)
def listar_jogos(
    nome: str | None = None,
    db: Session = Depends(get_db)
):
    consulta = db.query(Jogo)

    if nome:
        consulta = consulta.filter(
            Jogo.nome.ilike(f"%{nome}%")
        )

    return consulta.all()


@router.get(
    "/{id}",
    response_model=JogoResponseSchema
)
def buscar_jogo(
    id: int,
    db: Session = Depends(get_db)
):
    jogo = db.query(Jogo).filter(Jogo.id == id).first()

    if not jogo:
        raise HTTPException(
            status_code=404,
            detail="Jogo não encontrado."
        )

    return jogo


@router.post(
    "/",
    response_model=JogoResponseSchema,
    status_code=201
)
def cadastrar_jogo(
    jogo: JogoCreateSchema,
    db: Session = Depends(get_db)
):
    novo_jogo = Jogo(
        nome=jogo.nome,
        preco=jogo.preco,
        plataforma=jogo.plataforma,
        categoria_id=jogo.categoria_id
    )

    db.add(novo_jogo)
    db.commit()
    db.refresh(novo_jogo)

    return novo_jogo


@router.delete("/{id}")
def remover_jogo(
    id: int,
    db: Session = Depends(get_db)
):
    jogo = db.query(Jogo).filter(Jogo.id == id).first()

    if not jogo:
        raise HTTPException(
            status_code=404,
            detail="Jogo não encontrado."
        )

    db.delete(jogo)
    db.commit()

    return {
        "mensagem": "Jogo removido com sucesso."
    }