from typing import List

def wrap_text(text:str, width:int)->str:
    """Get text and width of wrap and return wrap text, 
    1 line with wrap length"""
    wrapped_text = ""
    current_line = ""
    line = ""
    for i in range(len(text)):
        if text[i] != " ":
            line += text[i]
        if text[i] == " " or i == len(text)-1:
            if len(current_line + " " + line) > width:
                wrapped_text += current_line + "\n"
                current_line = ""
            current_line += " " + line
            line = ""
    wrapped_text += current_line
    return wrapped_text

def find_substr(str1:str, substr:str):
    """Get string and substring, return 1 if substr in str == True, else 0"""
    for index_1 in range(len(str1) - len(substr) - 1):
        for index_2 in range(len(substr)):
            if substr[index_2] != str1[index_1 + index_2]:
                break
            if (substr[index_2] == str1[index_1 + index_2]) and (
                index_2 == len(substr) - 1
            ):
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
            tmp += wrapped_text[i]
            i += 1
        res.append(find_substr(tmp,subs))
        tmp = ""
        i += 1
    return res
