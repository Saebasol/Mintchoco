from dataclasses import dataclass
from typing import Literal, Optional

from mintchoco.types import HitomiFileJSON


@dataclass
class File:
    index_id: int
    name: str
    width: int
    height: int
    hash: str
    haswebp: Literal[0, 1]
    hasavifsmalltn: Optional[Literal[1]] = None
    hasavif: Optional[Literal[1]] = None
    id: Optional[int] = None

    def to_dict(self) -> HitomiFileJSON:
        hitomi_file_json = HitomiFileJSON(
            width=self.width,
            height=self.height,
            hash=self.hash,
            haswebp=self.haswebp,
            name=self.name,
        )

        if self.hasavif:
            hitomi_file_json["hasavif"] = self.hasavif
        if self.hasavifsmalltn:
            hitomi_file_json["hasavifsmalltn"] = self.hasavifsmalltn

        return hitomi_file_json

    @classmethod
    def from_dict(cls, index_id: int, d: HitomiFileJSON) -> "File":
        return cls(
            index_id=index_id,
            name=d["name"],
            width=d["width"],
            height=d["height"],
            hash=d["hash"],
            haswebp=d["haswebp"],
            hasavifsmalltn=d.get("hasavifsmalltn"),
            hasavif=d.get("hasavif"),
        )
