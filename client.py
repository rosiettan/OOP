# inheritance
from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass
class Client:
    id: UUID
    name: str

    @classmethod
    def from_name(cls, name: str) -> "Client":
        return cls(
            id=uuid4(),
            name=name,
        )
