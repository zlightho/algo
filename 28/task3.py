from math import sqrt, ceil


def TheRabbitsFoot(s: str, encode: bool) -> str:
    """gets the original string s and either encrypts it (encode = true)
    or decrypts it (encode = false),
    only of course without the original spaces."""
    string_no_space = ""
    for i in s:
        if i == " ":
            continue
        string_no_space += i

    side_length = ceil(sqrt(len(string_no_space)))
    matrix = []
    for i in range(side_length):
        row = []
        for j in range(side_length):
            row.append("")
        matrix.append(row)
    text_index = 0
    for i in range(side_length):
        for j in range(side_length):
            if text_index < len(string_no_space):
                matrix[j][i] = string_no_space[text_index]
                text_index += 1
    if encode:
        encoded_text = ""
        for i in range(side_length):
            for j in range(side_length):
                encoded_text += matrix[i][j]
            if i != side_length - 1:
                encoded_text += " "
        return encoded_text
    else:
        words = []
        word = ""
        for i in s:
            if i == " ":
                words.append(word)
                word = ""
            else:
                word += i
        if word != "":
            words.append(word)
        side_length = len(words)
        decoded_text = ""
        for i in range(len(words[0])):
            for j in range(side_length):
                if i < len(words[j]):
                    decoded_text += words[j][i]
        return decoded_text
