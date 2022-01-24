from typing import TypedDict

from mintchoco.types import HitomiGalleryinfoJSON, HitomiInfoJSON


class BaseHeliotropeJSON(TypedDict):
    status: int


class HeliotropeFileJSON(TypedDict):
    url: str
    name: str


class HeliotropeGalleryInfoJSON(BaseHeliotropeJSON, HitomiGalleryinfoJSON):
    ...


class HeliotropeInfoJSON(BaseHeliotropeJSON, HitomiInfoJSON):
    ...


class HeliotropeImageJSON(BaseHeliotropeJSON):
    files: list[HeliotropeFileJSON]


class HeliotropeListJSON(BaseHeliotropeJSON):
    list: list[HitomiInfoJSON]
    total: int


class HeliotropeRandomJSON(HeliotropeInfoJSON):
    ...


class HeliotropeSearchJSON(BaseHeliotropeJSON):
    result: list[HitomiInfoJSON]
    count: int
