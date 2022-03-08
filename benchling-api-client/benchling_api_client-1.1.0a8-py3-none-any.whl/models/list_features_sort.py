from enum import Enum
from functools import lru_cache
from typing import cast

from ..extensions import Enums


class ListFeaturesSort(Enums.KnownString):
    NAME = "name"
    NAMEASC = "name:asc"
    NAMEDESC = "name:desc"

    def __str__(self) -> str:
        return str(self.value)

    @staticmethod
    @lru_cache(maxsize=None)
    def of_unknown(val: str) -> "ListFeaturesSort":
        if not isinstance(val, str):
            raise ValueError(f"Value of ListFeaturesSort must be a string (encountered: {val})")
        newcls = Enum("ListFeaturesSort", {"_UNKNOWN": val}, type=Enums.UnknownString)  # type: ignore
        return cast(ListFeaturesSort, getattr(newcls, "_UNKNOWN"))
