from typing import TypeVar

__all__ = ("corresponding_pairs",)


T1 = TypeVar("T1")
T2 = TypeVar("T2")


def corresponding_pairs(arr1: list[T1], arr2: list[T2]) -> list[tuple[T1, T2]]:
    """Формирует список пар из пары списков.

    Example:
        >> corresponding_pairs([1, 2], [3, 4])
        [(1, 3), (2, 4)]
    """
    if arr1 == [] or arr2 == []:
        return []
    
    result = []
    for i, (itm1, item2) in enumerate(zip(arr1, arr2)):
        result.append((itm1, item2))

    return result

corresponding_pairs([1,], [3, 4])