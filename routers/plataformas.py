from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Plataforma


router = APIRouter(
    prefix="/plataformas",
    tags=["Plataformas"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.get("/")
def listar_plataformas(
    db: Session = Depends(get_db)
):

    plataformas = db.query(Plataforma).all()

    return plataformas