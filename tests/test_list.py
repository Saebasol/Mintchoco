from mintchoco.client import Mintchoco

import pytest


@pytest.mark.asyncio
async def test_list(client: Mintchoco):
    resp = await client.list(1)
    assert resp.list
