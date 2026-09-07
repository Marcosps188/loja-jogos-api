from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Categoria


router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.get("/")
def listar_categorias(
    db: Session = Depends(get_db)
):

    categorias = db.query(Categoria).all()

    return categorias