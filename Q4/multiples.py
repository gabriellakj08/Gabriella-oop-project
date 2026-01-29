def is_one_multiple_of_other(a: int, b: int) -> bool:

    if a == 0 and b == 0:
        return True

    if a == 0 and b != 0:
        return True
    if b == 0 and a != 0:
        return True


    if a % b == 0 or b % a == 0:
        return True

    return False