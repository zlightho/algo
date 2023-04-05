def SherlockValidString(s: str) -> bool:
    """
    Determines whether a given string is valid based on the following conditions:
    - All letters occur an equal number of times;
    - It is allowed to remove one letter to make the frequency of all letters equal.

    Args:
        s (str): The input string consisting of Latin letters.

    Returns:
        bool: True if the string is valid, False otherwise.

    Examples:
        >>> is_valid_password("xyz")
        True
        >>> is_valid_password("xyzaa")
        True
        >>> is_valid_password("xxyyz")
        True
        >>> is_valid_password("xyzzz")
        False
        >>> is_valid_password("xxyyza")
        False
        >>> is_valid_password("xxyyzabc")
        False
    """
    letter_freq = {}
    for letter in s:
        if letter in letter_freq:
            letter_freq[letter] += 1
        else:
            letter_freq[letter] = 1

    freq_values = list(set(letter_freq.values()))
    
    if len(freq_values) == 1:
        return True

    if len(freq_values) != 2:
        return False

    min_freq, max_freq = sorted(freq_values)
    freq_diff = max_freq - min_freq

    return (min_freq == 1 and list(letter_freq.values()).count(min_freq) == 1) or (freq_diff == 1 and list(letter_freq.values()).count(max_freq) == 1)