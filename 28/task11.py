def LineAnalysis(line):
    dot_groups = []  # A list to store groups of consecutive dots
    star_groups = []  # A list to store groups of consecutive stars
    current_dots = ""  # A temporary variable to accumulate consecutive dots
    current_stars = ""  # A temporary variable to accumulate consecutive stars

    for i in range(len(line)):
        if line[i] == "*":
            current_stars += "*"
        if line[i] == "." and current_stars != "":
            star_groups.append(current_stars)
            current_stars = ""
        if line[i] == ".":
            current_dots += "."
        if line[i] == "*" and current_dots != "":
            dot_groups.append(current_dots)
            current_dots = ""
        if i == len(line) - 1:
            star_groups.append(current_stars)

    # Check if all groups of stars and dots are consistent
    # and if the line starts and ends with an asterisk
    if (
        star_groups[1:] == star_groups[:-1]
        and dot_groups[1:] == dot_groups[:-1]
        and line[0] == "*"
        and line[-1] == "*"
    ):
        return True
    else:
        return False
