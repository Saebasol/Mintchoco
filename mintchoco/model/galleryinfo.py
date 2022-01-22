from dataclasses import dataclass, field
from typing import Optional

from mintchoco.model.file import File
from mintchoco.model.tag import Tag
from mintchoco.types import HitomiGalleryinfoJSON


@dataclass
class Galleryinfo:
    id: int
    title: str
    japanese_title: Optional[str]
    language: Optional[str]
    language_localname: str
    type: str
    date: str
    files: list[File] = field(default_factory=list)
    tags: list[Tag] = field(default_factory=list)

    def to_dict(self) -> HitomiGalleryinfoJSON:
        return HitomiGalleryinfoJSON(
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
    def from_dict(cls, d: HitomiGalleryinfoJSON) -> "Galleryinfo":
        int_id = int(d["id"])
        return cls(
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
