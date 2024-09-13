def find_first_blue(left: int, right: int) -> int:
    while left < right:
        pivot = (left + right) // 2
        if is_blue(pivot):
            right = pivot
        else:
            left = pivot + 1
    return left


def find_last_red(left: int, right: int) -> int:
    while left < right:
        pivot = (left + right + 1) // 2
        if is_red(pivot):
            left = pivot
        else:
            right = pivot - 1
    return left
