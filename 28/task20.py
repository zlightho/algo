def white_walkers(village: str) -> bool:
    pairs = [
        (i, j)
        for i in range(len(village))
        for j in range(i + 1, len(village))
        if village[i].isdigit()
        and village[j].isdigit()
        and int(village[i]) + int(village[j]) == 10
    ]

    for pair in pairs:
        if village[pair[0] + 1 : pair[1]].count("=") >= 3:
            return True
    return False
