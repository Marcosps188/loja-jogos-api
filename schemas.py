from pydantic import BaseModel, ConfigDict


class JogoCreateSchema(BaseModel):
    nome: str
    preco: float
    plataforma: str
    categoria_id: int


class JogoResponseSchema(BaseModel):
    id: int
    nome: str
    preco: float
    plataforma: str
    categoria_id: int

    model_config = ConfigDict(from_attributes=True)