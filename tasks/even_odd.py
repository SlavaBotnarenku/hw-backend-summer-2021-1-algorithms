__all__ = ("even_odd",)

lst = [1, 2, 3, 4, 5]

def even_odd(numbers: list[int]) -> float:
    """Определяет отношение суммы четных элементов списка
    к сумме нечетных.

    Example:
        >> even_odd([1, 2, 3, 4, 5])
        0.6667
    """
    def check_if_odd(num: int) -> bool:
        return True if num % 2 == 0 else False
    
    even_lst = []
    odd_lst = []
    for i in numbers:
        if check_if_odd(i):
            odd_lst.append(i)
        else:
            even_lst.append(i)

    if (sum(odd_lst) == 0) or (sum(even_lst) == 0):
        return 0

    return (sum(odd_lst) / sum(even_lst))

print(even_odd(lst))