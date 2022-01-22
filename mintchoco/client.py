from types import TracebackType
from typing import Any, Literal, Optional
from aiohttp import ClientSession

from mintchoco.model.galleryinfo import Galleryinfo
from mintchoco.model.image import Image
from mintchoco.model.info import Info
from mintchoco.types import HitomiGalleryinfoJSON, HeliotropeImageJSON, HitomiInfoJSON


class Client:
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

    async def galleryinfo(self, index: int) -> Galleryinfo:
        resp: HitomiGalleryinfoJSON = await self.request(
            "GET", f"/hitomi/galleryinfo/{index}"
        )
        return Galleryinfo.from_dict(resp)

    async def image(self, index: int) -> list[Image]:
        resp = await self.request("GET", f"/hitomi/image/{index}")
        image_list: list[HeliotropeImageJSON] = [x for x in resp["files"]]
        return [Image.from_dict(image) for image in image_list]

    async def info(self, index: int) -> Info:
        resp: HitomiInfoJSON = await self.request("GET", f"/hitomi/info/{index}")
        return Info.from_dict(resp)

    async def __aenter__(self) -> "Client":
        return self

    async def __aexit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        if self.client_session:
            await self.client_session.close()
