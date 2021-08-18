from os import getenv

import pytest
from mintchoco.client import Client


@pytest.fixture()
async def client():
    client = Client(getenv("hiyobot"))
    yield client
    if client.client_session:
        await client.client_session.close()
