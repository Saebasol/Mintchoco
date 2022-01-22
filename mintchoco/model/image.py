from dataclasses import dataclass

from mintchoco.types import HeliotropeImageJSON


@dataclass
class Image:
    name: str
    url: str

    def to_dict(self) -> HeliotropeImageJSON:
        return HeliotropeImageJSON(name=self.name, url=self.url)

    @classmethod
    def from_dict(cls, d: HeliotropeImageJSON) -> "Image":
        return cls(name=d["name"], url=d["url"])
