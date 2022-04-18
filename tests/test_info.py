from mintchoco.client import Mintchoco
from tests.constant import INFO
import pytest


@pytest.mark.asyncio
async def test_info(client: Mintchoco):
    info = await client.info(1)
    assert info
    assert info.to_dict() == INFO
