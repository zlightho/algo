def line_analysis(line: str) -> bool:
    # Check if the line starts and ends with an asterisk
    if line[0] != "*" or line[-1] != "*":
        return False

    # Check if the line contains only dots and asterisks
    for char in line[1:-1]:
        if char != "." and char != "*":
            return False

    # Check if the pattern of dots and asterisks is correct
    pattern = line[1:-1].split("*")
    if len(pattern) < 2 or any(len(p) != len(pattern[0]) for p in pattern):
        return False

    return True
