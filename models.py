from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base


class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, unique=True)


class Plataforma(Base):
    __tablename__ = "plataformas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, unique=True)


class Jogo(Base):
    __tablename__ = "jogos"

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String, nullable=False, index=True)

    preco = Column(Float, nullable=False)

    plataforma_id = Column(
        Integer,
        ForeignKey("plataformas.id"),
        nullable=False
    )

    categoria_id = Column(
        Integer,
        ForeignKey("categorias.id"),
        nullable=False
    )

    usuario = Column(String, nullable=False)

    data_inclusao = Column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )