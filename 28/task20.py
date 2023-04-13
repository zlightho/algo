def white_walkers(village: str) -> bool:
    pairs = []
    last_digit_idx = None
    for i in range(len(village)):
        if village[i].isdigit():
            if (
                last_digit_idx is not None
                and int(village[i]) + int(village[last_digit_idx]) == 10
            ):
                pairs.append((last_digit_idx, i))
            last_digit_idx = i
    for pair in pairs:
        if village[pair[0] + 1 : pair[1]].count("=") != 3:
            return False
    return len(pairs) > 0
