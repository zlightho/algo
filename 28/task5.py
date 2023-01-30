def BigMinus(s1, s2):
    """receives two numbers in string format as input (the numbers are always
    correct -- a set of digits), and returns the absolute value (modulus)
    of the difference -- the first number s1 minus the second number s2,
    also in string format."""
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    s1 = list(s1)
    s2 = list(s2)
    s2 = [0] * (len(s1) - len(s2)) + s2
    s = []
    res = ""
    transfer = 0
    for i in range(len(s1) - 1, -1, -1):
        d1 = int(s1[i])
        d2 = int(s2[i])
        if d1 - transfer < d2:
            s.append(str(d1 + 10 - d2 - transfer))
            transfer = 1
        else:
            s.append(str(d1 - d2 - transfer))
            transfer = 0
    while len(s) > 1 and s[-1] == "0":
        s.pop()
    for i in range(len(s) - 1, -1, -1):
        res += s[i]

    return res


print(BigMinus("321", "1"))
