from types import TracebackType
from typing import Any, Literal, Optional
from aiohttp import ClientSession
from mintchoco.base import (
    HeliotropeGalleryInfoJSON,
    HeliotropeImageJSON,
    HeliotropeInfoJSON,
    HeliotropeListJSON,
    HeliotropeRandomJSON,
    HeliotropeSearchJSON,
)


class MintchocoHttp:
    BASE_URL = "https://api.saebasol.org/api"

    def __init__(self, client_session: Optional[ClientSession] = None) -> None:
        self.client_session = client_session

    async def request(
        self,
        method: Literal["GET", "POST"],
        path: str,
        json: Optional[dict[str, Any]] = None,
    ) -> Any:
        url = self.BASE_URL + path

        if not self.client_session:
            self.client_session = ClientSession()

        async with self.client_session.request(method, url, json=json) as resp:
            return await resp.json()

    async def galleryinfo(self, index: int) -> HeliotropeGalleryInfoJSON:
        return await self.request("GET", f"/hitomi/galleryinfo/{index}")

    async def image(self, index: int) -> HeliotropeImageJSON:
        return await self.request("GET", f"/hitomi/image/{index}")

    async def info(self, index: int) -> HeliotropeInfoJSON:
        return await self.request("GET", f"/hitomi/info/{index}")

    async def list(self, index: int) -> HeliotropeListJSON:
        return await self.request("GET", f"/hitomi/list/{index}")

    async def random(self) -> HeliotropeRandomJSON:
        return await self.request("GET", "/hitomi/random")

    async def search(self, query: list[str], offset: int = 0) -> HeliotropeSearchJSON:
        return await self.request(
            "POST",
            "/hitomi/search",
            {
                "query": query,
                "offset": offset,
            },
        )

    async def __aenter__(self) -> "MintchocoHttp":
        return self

    async def __aexit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        if self.client_session:
            await self.client_session.close()
