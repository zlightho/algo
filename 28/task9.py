def TankRush(H1: int, W1: int, S1: str, H2: int, W2: int, S2: str) -> bool:
    """With the first three parameters it gets the source map,
    and with the next three parameters it gets the map that is searched
    for in the source. TankRush returns true if the second map is
    contained within the first.
    """
    # First, convert the input strings into lists for easier manipulation
    grid1 = [list(row) for row in S1.split()]
    grid2 = [list(row) for row in S2.split()]

    # Check if grid2 is smaller than grid1
    if H2 > H1 or W2 > W1:
        return False

    # Iterate over all possible positions of grid2 in grid1
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            # Check if the subgrid of grid1 at position (i, j) matches grid2
            if all(
                grid1[i + di][j + dj] == grid2[di][dj]
                for di in range(H2)
                for dj in range(W2)
            ):
                return True

    # If we haven't found a match by now,
    # it means grid2 is not contained in grid1
    return False
