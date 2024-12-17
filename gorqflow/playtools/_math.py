def add_one(x: int) -> int:
    """Add one to an integer

    Args:
        x (int): The base value

    Returns:
        int: x + 1
    """
    return x + 1


def sub_one(x: int) -> int:
    """Subtract one from an integer

    Args:
        x (int): The base value

    Returns:
        int: x - 1
    """
    return x - 1


def divide(nominator: int | float, denominator: int | float) -> float:
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return nominator / denominator
