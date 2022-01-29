from dataclasses import dataclass, field
from typing import Optional

from mintchoco.model.file import File
from mintchoco.model.tag import Tag


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
