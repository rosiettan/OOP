# inheritance
from abc import ABC, abstractmethod
from decimal import Decimal
from dataclasses import dataclass
from uuid import UUID, uuid4

from client import Client

@dataclass
class Transaction(ABC):
    id: UUID
    client_source: Client
    client_target: Client
    amount: Decimal # it's important to use decimal for money
    complete: bool

    def mark_as_complete(self):
        if self.amount > 0:
            self.complete = True

    @abstractmethod
    def save_to_database(self):
        ...

@dataclass
class CardTransaction(Transaction): # inherit from transaction
    card_number: str

    @classmethod
    def new_transaction(
            cls,
            client_source: Client,
            client_target: Client,
            amount: Decimal,
            card_number: str,
    ):
        return cls(
            id=uuid4(),
            client_source=client_source,
            client_target=client_target,
            amount=amount,
            complete=False,
            card_number=card_number,
        )

    def save_to_database(self):
        print("Saved Card Transaction", self.id)
        # self.amount *= 3

    def show_card_number(self):
        print(self.card_number)

@dataclass
class QRTransaction(Transaction):
    qr_number: str

    @classmethod
    def new_transaction(
            cls,
            client_source: Client,
            client_target: Client,
            amount: Decimal,
            qr_number: str,
    ):
        return cls(
            id=uuid4(),
            client_source=client_source,
            client_target=client_target,
            amount=amount,
            complete=False,
            qr_number=qr_number,
        )

    def save_to_database(self):
        print("Saved QR Transaction", self.id)
        # self.amount *= 2

