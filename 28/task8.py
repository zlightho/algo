from typing import List


def Unmanned(L: int, N: int, track: List[List[int]]) -> int:
    """receives the input length L of the road,
    the number of traffic lights on it N,
    and a description of the road itself,
    where each element consists of three values:
    the time relative to the beginning of the road
    (when a car arrives on a free road),
    the time when the red light is shown and the time when
    the green color is shown."""
    time = 0  # Current time
    pos = 0  # Current position
    if track[0][0] > L:
        return L

    for i in range(N):
        # Time required to reach the next traffic light
        time_to_reach = track[i][0] - pos
        time += time_to_reach

        # Time elapsed since the last green signal
        elapsed = time % (track[i][1] + track[i][2])

        # If the light is currently red or switching to green
        if elapsed < track[i][1]:
            # Wait for the light to turn green
            wait_time = track[i][1] - elapsed
            time += wait_time

        pos = track[i][0]  # Move to the next traffic light

    # Add the time to reach the end of the road
    time += L - pos

    return time
