from mintchoco.client import Mintchoco

import pytest


@pytest.mark.asyncio
async def test_search(client: Mintchoco):
    resp = await client.search(["sekigahara", "artist:tsukako"])
    assert resp.status == 200
