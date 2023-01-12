from typing import List


def ConquestCampaign(N: int, M: int, L: int, battalion: List[int]) -> int:
    """
    Gets the first two parameters the size of the bridgehead "Squares" NxM,
    and the battalion contains an array of L*2 integers (L>= 1)
    indexed from zero, in which each even (with an even index)
    element contains the next coordinate of the landing area
    in the first dimension N, and each odd (with an odd index) the element
    contains the next coordinate of the landing area in the second dimension M.
    """
    #  Initialize the territory to capture, fill in as False
    captured_territory = [[False for _ in range(M)] for _ in range(N)]
    # Initialize queue
    queue = []
    # Initialize counter days
    days = 0
    # Initialize counter captured points
    captured = 0
    # Processing the first landing
    for i in range(0, L * 2, 2):
        x, y = battalion[i] - 1, battalion[i + 1] - 1
        queue.append((x, y))
        captured_territory[x][y] = True
        captured += 1
    # While the queue is not empty
    # and the captured territory is smaller than the captured territory
    while len(queue) > 0 and captured < N * M:
        days += 1
        new_queue = []
        # Go through all possible movements
        for x, y in queue:
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                # Check that the new point does not go beyond the map
                if x + dx < 0 or x + dx >= N or y + dy < 0 or y + dy >= M:
                    continue
                # Сheck that it has not been captured yet
                if captured_territory[x + dx][y + dy]:
                    continue
                # Mark the point as captured
                captured_territory[x + dx][y + dy] = True
                # Increasing the counter of captured points
                captured += 1
                new_queue.append((x + dx, y + dy))
                # Starting a new loop with a new array
        queue = new_queue

    return days + 1
