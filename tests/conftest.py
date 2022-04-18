import pytest_asyncio

from mintchoco.client import Mintchoco

@pytest_asyncio.fixture()
async def client():
    async with Mintchoco() as client:
        yield client
