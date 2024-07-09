from client import Client


def test_client_create():
    client = Client.from_name(name="John")
    assert isinstance(client, Client)
    assert client.name == "John"

# it's important to name "test"