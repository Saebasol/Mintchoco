from dataclasses import dataclass
from typing import Literal, Optional

from mintchoco.types import HitomiTagJSON


@dataclass
class Tag:
    index_id: int
    male: Optional[Literal["", "1"]]
    female: Optional[Literal["", "1"]]
    tag: str
    url: str
    id: Optional[int] = None

    def to_dict(self) -> HitomiTagJSON:
        hitomi_tag_json = HitomiTagJSON(url=self.url, tag=self.tag)

        if self.male:
            hitomi_tag_json["male"] = self.male
        if self.female:
            hitomi_tag_json["female"] = self.female

        return hitomi_tag_json

    @classmethod
    def from_dict(cls, index_id: int, d: HitomiTagJSON) -> "Tag":
        return cls(
            index_id=index_id,
            male=d.get("male"),
            female=d.get("female"),
            tag=d["tag"],
            url=d["url"],
        )
