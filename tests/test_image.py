from mintchoco.client import Mintchoco
from tests.constant import IMAGE

import pytest


@pytest.mark.asyncio
async def test_image(client: Mintchoco):
    image = await client.image(1)
    assert image
    assert image.to_dict() == IMAGE
