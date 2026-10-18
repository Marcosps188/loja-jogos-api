from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    model_validator,
)
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, field_validator
from datetime import datetime
from pydantic import ValidationError


def validar_texto(valor: str, campo: str) -> str:
    valor = valor.strip()

    if not valor:
        raise ValueError(
            f"O campo {campo} é obrigatório e não pode ficar em branco."
        )

    if len(valor) < 3:
        raise ValueError(
            f"O campo {campo} deve conter pelo menos 3 caracteres."
        )

    if len(valor) > 100:
        raise ValueError(
            f"O campo {campo} deve conter no máximo 100 caracteres."
        )

    return valor


class SchemaBase(BaseModel):

    @model_validator(mode="before")
    @classmethod
    def validar_campos_obrigatorios(cls, dados):
        if not isinstance(dados, dict):
            return dados

        campos_texto = {
            "nome": "nome",
            "usuario": "usuário",
        }

        for campo, descricao in campos_texto.items():
            if campo in cls.model_fields and campo in dados:
                valor = dados[campo]

                if isinstance(valor, str) and not valor.strip():
                    raise ValueError(
                        f"O campo {descricao} é obrigatório "
                        "e não pode ficar em branco."
                    )

        return dados


class JogoCreateSchema(SchemaBase):
    nome: str = Field(min_length=3, max_length=100)
    preco: float = Field(gt=0)
    plataforma_id: int = Field(gt=0)
    categoria_id: int = Field(gt=0)
    usuario: str = Field(min_length=3, max_length=100)

    @field_validator("nome", mode="before")
    @classmethod
    def validar_nome(cls, valor):
        if isinstance(valor, str):
            return validar_texto(valor, "nome")
        return valor

    @field_validator("usuario", mode="before")
    @classmethod
    def validar_usuario(cls, valor):
        if isinstance(valor, str):
            return validar_texto(valor, "usuário")
        return valor 
    @field_validator("preco", mode="before")
    @classmethod
    def validar_preco(cls, valor):
        if isinstance(valor, (int, float)) and valor <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        return valor

    @field_validator("plataforma_id", "categoria_id", mode="before")
    @classmethod
    def validar_ids(cls, valor):
        if isinstance(valor, int) and valor <= 0:
            raise ValueError("O identificador deve ser um número positivo.")
        return valor


class JogoUpdateSchema(SchemaBase):
    nome: str = Field(min_length=3, max_length=100)
    preco: float = Field(gt=0)
    plataforma_id: int = Field(gt=0)

    
    @field_validator("nome", mode="before")
    @classmethod
    def validar_nome(cls, valor):
        if isinstance(valor, str):
            return validar_texto(valor, "nome")
        return valor

    @field_validator("preco", mode="before")
    @classmethod
    def validar_preco(cls, valor):
        if isinstance(valor, (int, float)) and valor <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        return valor

    @field_validator("plataforma_id", mode="before")
    @classmethod
    def validar_id(cls, valor):
        if isinstance(valor, int) and valor <= 0:
            raise ValueError(
                "O identificador da plataforma deve ser positivo."
            )
        return valor

    


class JogoResponseSchema(BaseModel):
    id: int
    nome: str
    preco: float
    plataforma_id: int
    categoria_id: int
    usuario: str
    data_inclusao: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
