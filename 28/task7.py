from typing import List


def hex_to_dec(number: int) -> int:
    """Function from hex to dec"""
    hex_digits = "0123456789ABCDEF"
    result = 0
    for digit in number:
        for i in range(len(hex_digits)):
            if digit == hex_digits[i]:
                result = result * 16 + i
                break
    return result


def oct_to_dec(number: int) -> int:
    """Function from oct to dec"""
    result = 0
    for digit in number:
        result = result * 8 + int(digit)
    return result


def UFO(N: int, data: List[int], octal: bool) -> List[int]:
    """Get the input length N of the digital traffic record, the traffic itself
    (a sequence of positive numbers) in the data array, and the octal flag,
    which specifies the number system of the input data: octal if octal = true,
    and hexadecimal otherwise.
    The function returns an array of length N containing the original numbers
    converted to decimal notation."""
    dec_data = []
    if octal:
        for number in data:
            dec_data.append(oct_to_dec(str(number)))
    else:
        for number in data:
            dec_data.append(hex_to_dec(str(number)))
    return dec_data
