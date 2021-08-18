from mintchoco.client import Client
import pytest


@pytest.mark.asyncio
async def test_galleryinfo(client: Client):
    res = await client.galleryinfo(1496588)
    assert res.status == 200


@pytest.mark.asyncio
async def test_info(client: Client):
    res = await client.info(1496588)
    assert res.status == 200


@pytest.mark.asyncio
async def test_list(client: Client):
    res = await client.list(1)
    assert res.status == 200


@pytest.mark.asyncio
async def test_images(client: Client):
    res = await client.images(1496588)
    assert res.status == 200


@pytest.mark.asyncio
async def test_search(client: Client):
    res = await client.search(["세키가하라"])
    assert res.status == 200
