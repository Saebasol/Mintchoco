from types import TracebackType
from typing import Any, Literal, Optional, cast
from aiohttp import ClientSession
from mintchoco.base_types import (
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
            if resp.status != 200:
                return None

            return await resp.json()

    async def get_galleryinfo(self, index: int) -> Optional[HeliotropeGalleryInfoJSON]:
        return cast(
            Optional[HeliotropeGalleryInfoJSON],
            await self.request("GET", f"/hitomi/galleryinfo/{index}"),
        )

    async def get_image(self, index: int) -> Optional[HeliotropeImageJSON]:
        return cast(
            Optional[HeliotropeImageJSON],
            await self.request("GET", f"/hitomi/image/{index}"),
        )

    async def get_info(self, index: int) -> Optional[HeliotropeInfoJSON]:
        return cast(
            Optional[HeliotropeInfoJSON],
            await self.request("GET", f"/hitomi/info/{index}"),
        )

    async def get_list(self, index: int) -> HeliotropeListJSON:
        return cast(
            HeliotropeListJSON, await self.request("GET", f"/hitomi/list/{index}")
        )

    async def get_random(self) -> HeliotropeRandomJSON:
        return cast(HeliotropeRandomJSON, await self.request("GET", "/hitomi/random"))

    async def get_search(self, query: list[str], offset: int) -> HeliotropeSearchJSON:
        return cast(
            HeliotropeSearchJSON,
            await self.request(
                "POST",
                "/hitomi/search",
                {
                    "query": query,
                    "offset": offset,
                },
            ),
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
