from typing import Self


class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    @classmethod
    def plus(cls, v1: Self, v2: Self) -> Self:
        return cls(v1.x + v2.x, v1.y + v2.y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    @classmethod
    def minus(cls, v1: Self, v2: Self) -> Self:
        return cls(v1.x - v2.x, v1.y - v2.y)

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y})"
