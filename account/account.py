from dataclasses import dataclass
from decimal import Decimal
from typing import Optional
from uuid import UUID, uuid4
import json
import random


'''
account - создает аккаунт с характеристиками айди, валюта, балас
здесь также функции перевода данных в формать джейсон и обратно
функция провеки
функция генерации рандомных данных для аккаунтов
'''


# Класс ошибки неидентичности валют
class CurrencyMismatchError(ValueError):
    pass


@dataclass
# Объявление классса Аккаунт (его тела)и его полей - их типы
class Account:
    id_: Optional[UUID]
    currency: str
    balance: Decimal

    # Инструкция для проверки баланса аккаунтов с условным оператором по признаку совпадения валюты
    def __lt__(self, other: "Account") -> bool:
        assert isinstance(other, Account)
        if self.currency != other.currency:
            raise CurrencyMismatchError
        return self.balance < other.balance

    # функция перевода данных в джейсон формат
    def to_json(self) -> str:
        json_repr = {
            "id": str(self.id_),
            "currency": self.currency,
            "balance": float(self.balance),
        }
        return json.dumps(json_repr)

    @classmethod
    # функция который генерирует объекты
    def from_json(cls, json_str: str) -> "Account": # Factory
        obj = json.loads(json_str)
        assert "currency" in obj
        assert "balance" in obj
        # Можно вместо assert писать и так"
        if "id" not in obj:
            raise ValueError("id should be in json string!")

        return Account(
            id_=UUID(obj["id"]),
            currency=obj["currency"],
            balance=Decimal(obj["balance"]),
        )

    @classmethod
    # функция который генерирует объекты с рандомным балансом от 1 до 1000
    def random(cls) -> "Account":   #Factory
        return Account(
            id_=uuid4(),
            currency="KZT",
            balance=Decimal(random.randint(1, 1000)),
        )
