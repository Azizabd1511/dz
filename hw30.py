from typing import List, Dict
from pydantic import BaseModel

class User(BaseModel):
    name: str
    mail: str
    address: str

user1 = User(name='Aziz', mail='azizqwerty123@mail.ru', address='Улица Аккурган, дом 155, кв 500')
print(vars(user1))


class Banks(BaseModel):

    bank_name: str
    bank_rating: int
    bank_opened: float

Banks1 = Banks(bank_name='TBC', bank_rating=9, bank_opened=10.30)
print(vars(Banks1))

class Cards(BaseModel):

    cardholder: Dict[str, int] = []
    which_bank: List[str] = []
    opened: float
cards1 = Cards(opened=6.00)
print(vars(cards1))




