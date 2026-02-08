__all__ = ("is_prime",)


def is_prime(number: int) -> bool:
    """Определяет, является ли число простым.

    Example:
        >> is_prime(0):
        False
        >> is_prime(1):
        False
        >> is_prime(4):
        True
    """
    if number in [0,1]:
        return False
    else:
        count = 0
        for i in range(2, number):
            print(f'{i} результат {number // i} или {number % i}')
            if (number % i) == 0:
                return False
            
        else:
            return True
