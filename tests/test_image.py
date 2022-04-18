from mintchoco.client import Mintchoco
import pytest


@pytest.mark.asyncio
async def test_image(client: Mintchoco):
    image = await client.image(1)
    assert image
    assert image.status == 200
