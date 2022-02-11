from dataclasses import dataclass

from mintchoco.model.info import Info


@dataclass
class List:
    list: list[Info]
    total: int
