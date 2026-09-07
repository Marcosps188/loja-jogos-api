from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Jogo, Plataforma, Categoria
from schemas import (
    JogoCreateSchema,
    JogoUpdateSchema,
    JogoResponseSchema
)


router = APIRouter(
    prefix="/jogos",
    tags=["Jogos"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# POST - Cadastrar jogo
@router.post("/", response_model=JogoResponseSchema)
def criar_jogo(
    jogo: JogoCreateSchema,
    db: Session = Depends(get_db)
):

    # Verifica se a plataforma existe
    plataforma = db.query(Plataforma).filter(
        Plataforma.id == jogo.plataforma_id
    ).first()

    if not plataforma:
        raise HTTPException(
            status_code=404,
            detail="Plataforma não cadastrada."
        )

    # Verifica se a categoria existe
    categoria = db.query(Categoria).filter(
        Categoria.id == jogo.categoria_id
    ).first()

    if not categoria:
        raise HTTPException(
            status_code=404,
            detail="Categoria não cadastrada."
        )

    novo_jogo = Jogo(
        nome=jogo.nome,
        preco=jogo.preco,
        plataforma_id=jogo.plataforma_id,
        categoria_id=jogo.categoria_id,
        usuario=jogo.usuario
    )

    db.add(novo_jogo)
    db.commit()
    db.refresh(novo_jogo)

    return novo_jogo


# GET - Listar todos os jogos
@router.get("/", response_model=list[JogoResponseSchema])
def listar_jogos(
    db: Session = Depends(get_db)
):

    jogos = db.query(Jogo).all()

    return jogos


# GET - Buscar jogo pelo ID
@router.get("/{jogo_id}", response_model=JogoResponseSchema)
def buscar_jogo(
    jogo_id: int,
    db: Session = Depends(get_db)
):

    jogo = db.query(Jogo).filter(
        Jogo.id == jogo_id
    ).first()

    if not jogo:
        raise HTTPException(
            status_code=404,
            detail="Jogo não encontrado."
        )

    return jogo


# PUT - Atualizar jogo
@router.put("/{jogo_id}", response_model=JogoResponseSchema)
def atualizar_jogo(
    jogo_id: int,
    jogo_atualizado: JogoUpdateSchema,
    db: Session = Depends(get_db)
):

    # Procura o jogo
    jogo = db.query(Jogo).filter(
        Jogo.id == jogo_id
    ).first()

    if not jogo:
        raise HTTPException(
            status_code=404,
            detail="Jogo não encontrado."
        )

    # Verifica se a plataforma existe
    plataforma = db.query(Plataforma).filter(
        Plataforma.id == jogo_atualizado.plataforma_id
    ).first()

    if not plataforma:
        raise HTTPException(
            status_code=404,
            detail="Plataforma não cadastrada."
        )

    # Atualiza SOMENTE os campos permitidos
    jogo.nome = jogo_atualizado.nome
    jogo.preco = jogo_atualizado.preco
    jogo.plataforma_id = jogo_atualizado.plataforma_id

    db.commit()
    db.refresh(jogo)

    return jogo


# DELETE - Excluir jogo
@router.delete("/{jogo_id}")
def deletar_jogo(
    jogo_id: int,
    db: Session = Depends(get_db)
):

    jogo = db.query(Jogo).filter(
        Jogo.id == jogo_id
    ).first()

    if not jogo:
        raise HTTPException(
            status_code=404,
            detail="Jogo não encontrado."
        )

    db.delete(jogo)
    db.commit()

    return {
        "mensagem": "Jogo excluído com sucesso."
    }