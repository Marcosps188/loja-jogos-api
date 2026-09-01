from sqlalchemy import Column, Integer, String, Float
from database import Base


class Jogo(Base):
    __tablename__ = "jogos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, index=True)
    preco = Column(Float, nullable=False)
    plataforma = Column(String, nullable=False)
    categoria_id = Column(Integer, nullable=False)