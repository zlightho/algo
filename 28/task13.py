from typing import List


def ShopOLAP(N: int, items: List[str]) -> dict:
    """
    receives N >= 1 rows about products in the above format as input,
    and outputs an array of length M <= N containing a sales summary
    in grouped form.
    """
    result_dict = {}
    for i in items:
        split_list = i.split()
        key, value = split_list[0], int(split_list[1])
        if key in result_dict:
            result_dict[key] += value
        else:
            result_dict[key] = value
    sorted_result_list = sorted(
        result_dict.items(), key=lambda x: (-x[1], x[0])
    )
    formatted_result = [f"{key} {value}" for key, value in sorted_result_list]
    return formatted_result
