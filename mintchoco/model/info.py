from dataclasses import dataclass
from typing import Optional

from mintchoco.types import HitomiInfoJSON


@dataclass
class Info:
    id: int
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

    def to_dict(self) -> HitomiInfoJSON:
        return HitomiInfoJSON(
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
    def from_dict(cls, d: HitomiInfoJSON) -> "Info":
        return cls(
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
