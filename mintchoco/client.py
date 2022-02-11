from typing import Optional, List

from aiohttp import ClientSession

from mintchoco.http import MintchocoHttp
from mintchoco.model.base import (
    HeliotropeImage,
    HeliotropeInfo,
    HeliotropeList,
    HeliotropeSearch,
)


class Mintchoco(MintchocoHttp):
    def __init__(self, client_session: Optional[ClientSession] = None) -> None:
        super().__init__(client_session)

    async def image(self, index: int) -> Optional[HeliotropeImage]:
        if resp := await self.get_image(index):
            return HeliotropeImage.from_dict(resp)
        return None

    async def info(self, index: int) -> Optional[HeliotropeInfo]:
        if resp := await self.get_info(index):
            return HeliotropeInfo.from_dict(resp)
        return None

    async def list(self, index: int) -> Optional[HeliotropeList]:
        if resp := await self.get_list(index):
            return HeliotropeList.from_dict(resp)
        return None

    async def random(self) -> HeliotropeInfo:
        return HeliotropeInfo.from_dict(await self.get_random())

    async def search(
        self, query: List[str], offset: int = 0
    ) -> Optional[HeliotropeSearch]:
        if resp := await self.get_search(query, offset):
            return HeliotropeSearch.from_dict(resp)
        return None
