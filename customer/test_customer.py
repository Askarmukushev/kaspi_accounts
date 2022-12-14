from decimal import Decimal
from uuid import uuid4
import pytest

from account.account import Account
from customer.customer import Customer


class TestCustomer:
    def test_two_plus_two(self) -> None:
        assert 2 + 2 == 4

    def test_customer_create(self) -> None:
        customer_id = uuid4()
        customer = Customer(
            id_=customer_id,
            first_name="Askar",
            last_name="Mukushev",
            age=25,
            accounts=[],
        )

        assert customer.id_ == customer_id
        assert customer.first_name == "Askar"
        assert customer.last_name == "Mukushev"

        customer2 = Customer(
            id_=customer_id,
            first_name="Askar",
            last_name="Mukushev",
            age=25,
            accounts=[],
        )

        assert customer == customer2
        assert id(customer) != id(customer2)

        assert customer < customer2

    def test_customer_create_with_accounts(self) -> None:
        account1_id = uuid4()
        account2_id = uuid4()
        account1 = Account(
            id_=account1_id,
            currency="KZT",
            balance=Decimal(1000),
        )
        account2 = Account(
            id_=account2_id,
            currency="KZT",
            balance=Decimal(500),
        )
