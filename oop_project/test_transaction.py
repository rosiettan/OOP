from decimal import Decimal

from client import Client
from transaction import Transaction, TransactionState


def test_transaction_create():
    client1 = Client.from_name("John")
    client2 = Client.from_name("Bill")

    transaction = Transaction.new_transaction(
        client_from=client1,
        client_to=client2,
        amount=Decimal(100),
    )

    assert isinstance(transaction, Transaction)
    assert transaction.client_from.name == "John"
    assert transaction.client_to.name == "Bill"


def test_transaction_incorrect():
    client1 = Client.from_name("John")
    client2 = Client.from_name("Bill")

    transaction = Transaction.new_transaction(
        client_from=client1,
        client_to=client2,
        amount=Decimal(-100),
    )

    assert isinstance(transaction, Transaction)
    assert transaction.client_from.name == "John"
    assert transaction.client_to.name == "Bill"
    assert transaction.state == TransactionState.ERROR
