from typing import List

def wrap_text(text, width):
    wrapped_text = ""
    current_line = ""
    word = ""
    i = 0
    while i < len(text) or word:
        if not word:
            while i < len(text) and text[i] != ' ':
                word += text[i]
                i += 1
            i += 1
            if i < len(text) and text[i] == ' ':
                i += 1
        if len(current_line) + len(word) + (1 if current_line else 0) <= width:
            current_line += (' ' if current_line else '') + word
            word = ''
        else:
            if current_line:
                wrapped_text += current_line + '\n'
                current_line = ''
                continue
            else:
                for j in range(0, len(word), width):
                    wrapped_text += word[j:j + width]
                    if j + width < len(word):
                        wrapped_text += '\n'
                word = ''
    current_line += word
    if current_line:
        wrapped_text += current_line
    return wrapped_text


def find_substr(str1:str, substr:str):
    """Get string and substring, return 1 if substr in str == True, else 0"""
    words = str1.split(" ")
    for word in words:
        if word == substr:
            return 1
    return 0



def WordSearch(length:int, s:str, subs:str) -> List[int]:
    """Get length of wrap, "s" as text, and subs for checking substring ir not in wraps
    return massive, with 1 and 0"""
    wrapped_text = wrap_text(s, length)
    tmp = ''
    res = []
    i = 0
    while i < len(wrapped_text):
        while i < len(wrapped_text) and wrapped_text[i] != '\n':
            if wrapped_text[i] == '\n':
                continue
            tmp += wrapped_text[i]
            i += 1
        res.append(find_substr(tmp,subs))
        tmp = ""
        i += 1
    return res
