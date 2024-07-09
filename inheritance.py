# inheritance
from decimal import Decimal
from uuid import uuid4
from client import Client
from transaction import CardTransaction, QRTransaction, Transaction

john = Client.from_name("John")
bill = Client.from_name("Bill")

transaction1 = CardTransaction.new_transaction(
    client_source=john,
    client_target=bill,
    amount=Decimal("100"),
    card_number="4404055165789526",
)

transaction2 = QRTransaction.new_transaction(
    client_source=john,
    client_target=bill,
    amount=Decimal(4),
    qr_number="snfkanfl546q2341a",
)

def save_to_database(transaction:Transaction):
    assert isinstance(transaction, Transaction)
    transaction.save_to_database()

save_to_database(transaction1)
save_to_database(transaction2)

# transaction.mark_as_complete()
# print(transaction)