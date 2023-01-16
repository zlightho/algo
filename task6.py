from typing import List


def PatternUnlock(N: int, hits: List[int]):
    """Gets the length of the array with unlock codes by parameter N,
    and the hits array itself contains a sequence of unlock codes -
    point numbers in the range from 1 to 9.
    And return length of the , without '0' """
    dist = 0
    for i in range(0, N-2):
        tmp = hits[i]
        next = hits[i+1]
        if (
            ((tmp == 6 or tmp == 4 or tmp == 7 or tmp == 9) and next == 2)
            or ((tmp == 1 or tmp == 3) and (next == 5 or next == 8))
            or ((tmp == 5 or tmp == 8) and (next == 1 or next == 3))
            or (tmp == 2 and (next == 6 or next == 9 or next == 4 or next == 7))
        ):
            dist += 1.4142135623730951
        else:
            dist += 1.0
    tmp = hits[-2]
    next = hits[-1]
    if (
        ((tmp == 6 or tmp == 4 or tmp == 7 or tmp == 9) and next == 2)
        or ((tmp == 1 or tmp == 3) and (next == 5 or next == 8))
        or ((tmp == 5 or tmp == 8) and (next == 1 or next == 3))
        or (tmp == 2 and (next == 6 or next == 9 or next == 4 or next == 7))
    ):
        dist += 1.4142135623730951
    else:
        dist += 1.0
    rounded_x = round(dist, 5)
    str_dist = str(rounded_x)
    final_dist = ''
    for i in str_dist:
        if i == '0' or i == '.':
            continue
        final_dist += i
    return final_dist

print(PatternUnlock(3, [2,1,9]))
