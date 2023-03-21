from typing import Optional

from pydantic import BaseModel

class Produto(BaseModel):
    id: Optional[int] = None
    titulo: str
    preco: float