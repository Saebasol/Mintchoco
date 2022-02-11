from typing import Literal,Optional, TypedDict, Union

class _HitomiFileJSONOptional(TypedDict, total=False):
    hasavifsmalltn: Literal[1]


class HitomiFileJSON(_HitomiFileJSONOptional):
    width: int
    hash: str
    haswebp: Literal[0, 1]
    hasavif: Literal[0, 1]
    name: str
    height: int


class _HitomiTagJSONOptional(TypedDict, total=False):
    male: Literal["", "1", 1]
    female: Literal["", "1", 1]


class HitomiTagJSON(_HitomiTagJSONOptional):
    url: str
    tag: str


class HitomiParodysJSON(TypedDict):
    parody: str
    url: str


class HitomiArtistsJSON(TypedDict):
    artist: str
    url: str


class HitomiCharatersJSON(TypedDict):
    character: str
    url: str


class HitomiGroupsJSON(TypedDict):
    group: str
    url: str


class HitomiLanguagesJSON(TypedDict):
    url: str
    name: str
    galleryid: str
    language_localname: str


class HitomiGalleryinfoJSON(TypedDict):
    # Union is for conversion.
    id: Union[str, int]
    # Literal["manga", "doujinshi", "gamecg", "aritstcg", "anime"]
    type: str
    # title
    title: str
    japanese_title: Optional[str]
    # video
    video: Optional[str]
    videofilename: Optional[str]
    # language
    language_url: Optional[str]
    language_localname: Optional[str]
    language: Optional[str]
    languages: list[HitomiLanguagesJSON]
    # tags
    artists: Optional[list[HitomiArtistsJSON]]
    characters: Optional[list[HitomiCharatersJSON]]
    parodys: Optional[list[HitomiParodysJSON]]
    groups: Optional[list[HitomiGroupsJSON]]
    files: list[HitomiFileJSON]
    tags: Optional[list[HitomiTagJSON]]
    # etc
    scene_indexes: list[int]
    related: list[int]
    date: str


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