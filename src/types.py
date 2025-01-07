from enum import StrEnum, auto, unique


@unique
class MediaTypeEnum(StrEnum):
    movie = auto()
    series = auto()
    cartoon = auto()

