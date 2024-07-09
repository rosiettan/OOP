from dataclasses import dataclass
from decimal import Decimal
from typing import Optional
from uuid import UUID

from client import Client
from transaction import Transaction, TransactionState


@dataclass
class Bank:
    clients: dict[UUID, Client]
    transactions: list[Transaction]

    @classmethod
    def new_bank(cls) -> "Bank":
        return cls(
            clients=dict(),
            transactions=list(),
        )

    def get_balance(self, client_id: UUID) -> Decimal:
        assert client_id in self.clients
        ...

    def new_transaction(
            self,
            client_to: Client,
            amount: Decimal,
            client_from: Optional[Client] = None,
    ) -> Transaction:
        ...

    def add_client(self, client: Client):
        ...

    def complete_transaction(
            self,
            transaction: Transaction,
    ):
        ...
