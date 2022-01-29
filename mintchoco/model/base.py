from dataclasses import dataclass

from mintchoco.base import (
    HeliotropeGalleryInfoJSON,
    HeliotropeImageJSON,
    HeliotropeInfoJSON,
    HeliotropeListJSON,
    HeliotropeSearchJSON,
)
from mintchoco.model.galleryinfo import Galleryinfo
from mintchoco.model.file import File
from mintchoco.model.image import Image
from mintchoco.model.info import Info
from mintchoco.model.search import Search
from mintchoco.model.tag import Tag
from mintchoco.model.list import List


@dataclass
class HeliotropeBaseModel:
    status: int


@dataclass
class HeliotropeGalleryinfo(HeliotropeBaseModel, Galleryinfo):
    def to_dict(self) -> HeliotropeGalleryInfoJSON:
        return HeliotropeGalleryInfoJSON(
            status=self.status,
            title=self.title,
            id=self.id,
            date=self.date,
            type=self.type,
            japanese_title=self.japanese_title,
            language=self.language,
            files=[file.to_dict() for file in self.files],
            language_localname=self.language_localname,
            tags=[tag.to_dict() for tag in self.tags],
        )

    @classmethod
    def from_dict(cls, d: HeliotropeGalleryInfoJSON) -> "HeliotropeGalleryinfo":
        int_id = int(d["id"])
        return cls(
            status=d["status"],
            id=int_id,
            title=d["title"],
            japanese_title=d["japanese_title"],
            language=d["language"],
            language_localname=d["language_localname"],
            type=d["type"],
            date=d["date"],
            files=[File.from_dict(int_id, file) for file in d["files"]],
            tags=[Tag.from_dict(int_id, tag) for tag in d["tags"]],
        )


@dataclass
class HeliotropeImage(HeliotropeBaseModel, Image):
    def to_dict(self) -> HeliotropeImageJSON:
        return HeliotropeImageJSON(status=self.status, files=self.files)

    @classmethod
    def from_dict(cls, d: HeliotropeImageJSON) -> "HeliotropeImage":
        return cls(status=d["status"], files=d["files"])


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
    def from_dict(cls, d: HeliotropeInfoJSON) -> "HeliotropeInfo":
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
