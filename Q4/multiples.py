def is_one_multiple_of_other(a: int, b: int) -> bool:

    if a == 0 or b == 0:
        return False

    if a % b == 0 or b % a == 0:
        return True

    return False
