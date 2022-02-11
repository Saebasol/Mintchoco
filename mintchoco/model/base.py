from dataclasses import dataclass

from mintchoco.base_types import (
    HeliotropeImageJSON,
    HeliotropeInfoJSON,
    HeliotropeListJSON,
    HeliotropeSearchJSON,
)
from mintchoco.model.image import HeliotropeImageElement, Image
from mintchoco.model.info import Info
from mintchoco.model.search import Search
from mintchoco.model.list import List


@dataclass
class HeliotropeBaseModel:
    status: int


@dataclass
class HeliotropeImage(HeliotropeBaseModel, Image):
    def to_dict(self) -> HeliotropeImageJSON:
        return HeliotropeImageJSON(
            status=self.status, files=[file.to_dict() for file in self.files]
        )

    @classmethod
    def from_dict(cls, d: HeliotropeImageJSON) -> "HeliotropeImage":
        return cls(
            status=d["status"],
            files=[HeliotropeImageElement.from_dict(d) for d in d["files"]],
        )


@dataclass
class HeliotropeInfo(HeliotropeBaseModel, Info):
    def to_dict(self) -> HeliotropeInfoJSON:
        return HeliotropeInfoJSON(
            status=self.status,
            id=self.id,
            title=self.title,
            thumbnail=self.thumbnail,
            artist=self.artist,
            group=self.group,
            type=self.type,
            language=self.language,
            series=self.series,
            character=self.character,
            tags=self.tags,
            date=self.date,
        )

    @classmethod
    def from_dict(cls, d: HeliotropeInfoJSON) -> "HeliotropeInfo":  # type: ignore[override]
        return cls(
            status=d["status"],
            id=int(d["id"]),
            title=d["title"],
            thumbnail=d["thumbnail"],
            artist=d["artist"],
            group=d["group"],
            type=d["type"],
            language=d["language"],
            series=d["series"],
            character=d["character"],
            tags=d["tags"],
            date=d["date"],
        )


@dataclass
class HeliotropeList(HeliotropeBaseModel, List):
    def to_dict(self) -> HeliotropeListJSON:
        return HeliotropeListJSON(
            status=self.status,
            list=[info.to_dict() for info in self.list],
            total=self.total,
        )

    @classmethod
    def from_dict(cls, d: HeliotropeListJSON) -> "HeliotropeList":
        return cls(
            status=d["status"],
            list=[Info.from_dict(info) for info in d["list"]],
            total=d["total"],
        )


@dataclass
class HeliotropeSearch(HeliotropeBaseModel, Search):
    def to_dict(self) -> HeliotropeSearchJSON:
        return HeliotropeSearchJSON(
            status=self.status,
            result=[info.to_dict() for info in self.result],
            count=self.count,
        )

    @classmethod
    def from_dict(cls, d: HeliotropeSearchJSON) -> "HeliotropeSearch":
        return cls(
            status=d["status"],
            result=[Info.from_dict(info) for info in d["result"]],
            count=d["count"],
        )
