from mintchoco.client import Mintchoco
from tests.constant import SEARCH

import pytest


@pytest.mark.asyncio
async def test_search(client: Mintchoco):
    resp = await client.search(["sekigahara", "artist:tsukako"])
    assert resp.to_dict() == SEARCH
