from pydantic import BaseModel
from typing import Optional

class Docs(BaseModel):
    name:Optional[str] = "Ennibee"
    description:Optional[str] = "Ennibee is an ecommerce website for fashions"
    website:Optional[str] = "https://ennibee.com"