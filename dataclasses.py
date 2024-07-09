# dataclasses
from dataclasses import dataclass

@dataclass
class Client:
    name: str
    city: str
    age: int

# class Client:
#     def __init__(self, name: str, city: str):
#         self.name = name
#         self.city = city
#
#     def __str__(self):
#         return f"{self.name} from {self.city} city"


client = Client(
    name = "Raziya",
    city = "Kentau",
    age = 19
)

print(client)

