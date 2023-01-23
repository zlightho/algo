from math import sqrt, ceil

def TheRabbitsFoot(s: str, encode: bool) -> str:
    string_no_space = ''
    for i in s:
        if i == ' ':
            continue
        string_no_space += i
            
    side_length = ceil(sqrt(len(string_no_space)))
    matrix = []
    for i in range(side_length):
        row = []
        for j in range(side_length):
            row.append('')
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
        decoded_text = ""
        for i in range(side_length):
            for j in range(side_length):
                if matrix[j][i]:
                    decoded_text += matrix[j][i]
        return decoded_text

        

print(TheRabbitsFoot('отдай мою кроличью лапку', True))
print(TheRabbitsFoot('омоюу толл дюиа акчп йрьк', False))