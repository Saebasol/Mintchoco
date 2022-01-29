from dataclasses import dataclass

from mintchoco.model.info import Info


@dataclass
class Search:
    result: list[Info]
    count: int
