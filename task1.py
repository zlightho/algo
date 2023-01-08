def squirrel(N:int) -> int:
    """Get as param digit N, and return first number factorial N!"""
    number = 1
    while N > 0:
        number = number * N
        N -=1
    while number > 9:
        number = number // 10
    return number
