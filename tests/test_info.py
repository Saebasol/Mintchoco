from mintchoco.client import Mintchoco
import pytest


@pytest.mark.asyncio
async def test_info(client: Mintchoco):
    info = await client.info(1)
    assert info
    assert info.status == 200
