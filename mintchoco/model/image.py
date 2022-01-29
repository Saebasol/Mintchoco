from dataclasses import dataclass

from mintchoco.base import HeliotropeFileJSON


@dataclass
class Image:
    files: list[HeliotropeFileJSON]
