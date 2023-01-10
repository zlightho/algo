from typing import List

def odometer(oksana: List[int]) -> int:
    """Get list with speeds and durations, and return sum of all traveled distance."""
    current_speed = oksana[0]
    distance = current_speed * oksana[1]
    if len(oksana) > 2:
        for i in range(2, len(oksana), 2):
            current_speed = oksana[i]
            current_total_time = oksana[i+1]
            movement_time = current_total_time - oksana[i-1]
            distance = distance + current_speed * movement_time
    return distance

print(odometer([20, 2, 30, 6, 10, 7])) # 170
