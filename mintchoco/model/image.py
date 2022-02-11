from dataclasses import dataclass

from mintchoco.base_types import HeliotropeFileJSON


@dataclass
class HeliotropeImageElement:
    url: str
    name: str

    def to_dict(self) -> HeliotropeFileJSON:
        return HeliotropeFileJSON(url=self.url, name=self.name)

    @classmethod
    def from_dict(cls, d: HeliotropeFileJSON) -> "HeliotropeImageElement":
        return cls(url=d["url"], name=d["name"])


@dataclass
class Image:
    files: list[HeliotropeImageElement]
