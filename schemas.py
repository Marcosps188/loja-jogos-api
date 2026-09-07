from pydantic import BaseModel, ConfigDict
from datetime import datetime


class JogoCreateSchema(BaseModel):
    nome: str
    preco: float
    plataforma_id: int
    categoria_id: int
    usuario: str


class JogoUpdateSchema(BaseModel):
    nome: str
    preco: float
    plataforma_id: int


class JogoResponseSchema(BaseModel):
    id: int
    nome: str
    preco: float
    plataforma_id: int
    categoria_id: int
    usuario: str
    data_inclusao: datetime | None = None

    model_config = ConfigDict(from_attributes=True)