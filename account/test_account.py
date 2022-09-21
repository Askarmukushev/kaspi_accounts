from decimal import Decimal
from uuid import uuid4, UUID

import pytest
import json

from account.account import Account, CurrencyMismatchError
'''
test_account - тестовый класс присваивает характеристикам айди, валюта, балас 
значения и осуществляет проверки
'''


class TestAccount:
    def test_account_create(self) -> None:
# Первый аккаунт и его данные, поля
        account = Account(
            id_=uuid4(),
            currency="KZT",
            balance=Decimal(10),
        )
# Обязательная проверка что элемент который мы создали явяляется типом Account
        assert isinstance(account, Account)
        # Проверка что баланс == 10
        assert account.balance == 10

# Второй аккаунт и его данные
        account2 = Account(
            id_=uuid4(),
            currency="KZT",
            balance=Decimal(5),
        )

# Проверка что у второго аккаунта баланс больше чем у первого при инструкции(в Аккаунт)с учетмо валюты
        assert account2 < account

# Блок с ошибкой по валютам, ниже обработчик пропустит, так как разные валюты при инструкции
    def test_errors(self) -> None:
        account = Account(
            id_=uuid4(),
            currency="KZT",
            balance=Decimal(10),
        )

        account2 = Account(
            id_=uuid4(),
            currency="USD",
            balance=Decimal(5),
        )

# Обрабатываем с инструкцией по проверки величины валюты
        with pytest.raises(CurrencyMismatchError):
            assert account2 < account

# Функция конвертации данных в джейсон формат
    def test_json_import_export(self) -> None:
        account = Account.random()

        json_account = account.to_json()
        assert json.loads(json_account) == {
            "id": str(account.id_),
            "currency": account.currency,
            "balance": account.balance,
        }

# Функция конвертации данных из джейсон формата
    def test_account_from_json(self) -> None:
        test_json = '{"id": "8dfade94-c5db-4fdb-8583-a3b8e38cd8dc", "currency": "KZT", "balance": 10.0}'

        account = Account.from_json(test_json)
# Проверки assert
        assert isinstance(account, Account)
        assert account.id_ == UUID("8dfade94-c5db-4fdb-8583-a3b8e38cd8dc")
        assert account.balance == Decimal(10)
        assert account.currency == "KZT"

# Заключительная проверка между конвертациями данных в джейсон и обратно
    def test_to_json_from_json(self) -> None:
        # Check all fields are serialized
        account = Account.random()
        account2 = Account.from_json(account.to_json())
        assert account2 == account
