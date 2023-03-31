def BiggerGreater(input: str) -> str:
    """
    Given a non-magical word consisting of 2 or more English or Russian
    lowercase letters, this function
    attempts to transform it into a magical word by performing any number of
    pairwise letter swaps,
    or returns an empty string if it is impossible to obtain a magical word.

    A magical word has two properties:
    1) It is lexicographically greater than the input word.
    2) It is the smallest lexicographically greater word that can be obtained
    by swapping a pair of letters.

    The input word can be compared using the standard lexicographic order,
    where 'a' is less than 'z', and 'а' is less than 'я'.

    Args:
    input (str): The input non-magical word containing 2 or more English or
    Russian lowercase letters.

    Returns:
    str: The resulting magical word or an empty string if it is impossible to
    create a magical word.

    Examples:
    >>> BiggerGreater("ая")
    "яа"
    >>> BiggerGreater("fff")
    ""
    >>> BiggerGreater("нклм")
    "нкмл"
    >>> BiggerGreater("вибк")
    "викб"
    >>> BiggerGreater("вкиб")
    "ибвк"
    """
    chars = list(input)
    i = len(chars) - 2

    while i >= 0 and chars[i] >= chars[i + 1]:
        i -= 1

    if i == -1:
        return ""

    j = len(chars) - 1
    while chars[j] <= chars[i]:
        j -= 1

    chars[i], chars[j] = chars[j], chars[i]
    chars[i + 1 :] = reversed(chars[i + 1 :])
    return "".join(chars)
