from typing import List


def MaximumDiscount(N: int, price: List[int]) -> int:
    total_sum = sum(price)
    sorted_price = sorted(price, reverse=True)
    disc_price_list = sum(
        [sorted_price[i] for i in range(len(price)) if (i + 1) % 3 != 0]
    )
    return total_sum - disc_price_list
