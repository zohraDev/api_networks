from typing import Union
from pydantic import BaseModel


class Operators(BaseModel):
    code: int
    name: str

    def __str__(self):
        return f'{self.name} : {self.code}'


class NetWorkOffers(BaseModel):

    id: int
    code: int
    long: float
    lat: float
    g2_offer: bool
    g3_offer: float
    g4_offer: float

    def __str__(self):
        return f'{self.code}'
