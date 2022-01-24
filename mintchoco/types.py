from typing import Literal, Optional, TypedDict, Union


class _HitomiFileJSONOptional(TypedDict, total=False):
    hasavifsmalltn: Literal[1]
    hasavif: Literal[1]


class HitomiFileJSON(_HitomiFileJSONOptional):
    width: int
    height: int
    hash: str
    haswebp: Literal[0, 1]
    name: str


class _HitomiTagJSONOptional(TypedDict, total=False):
    male: Optional[Literal["", "1"]]
    female: Optional[Literal["", "1"]]


class HitomiTagJSON(_HitomiTagJSONOptional):
    url: str
    tag: str


class HitomiGalleryinfoJSON(TypedDict):
    date: str
    title: str
    type: str
    japanese_title: Optional[str]
    language: Optional[str]
    files: list[HitomiFileJSON]
    id: Union[str, int]
    language_localname: str
    tags: list[HitomiTagJSON]


class HitomiInfoJSON(TypedDict):
    id: Union[str, int]
    title: str
    thumbnail: str
    artist: list[str]
    group: list[str]
    type: str
    language: Optional[str]
    series: list[str]
    character: list[str]
    tags: list[str]
    date: str
