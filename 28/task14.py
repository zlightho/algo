list_undo = []
list_redo = []
current_str = ""
last_was_undo = False


def append(cmd: str) -> str:

    global current_str, last_was_undo, list_undo, list_redo

    if not last_was_undo:
        list_undo.append(current_str)
    else:
        list_redo = []
        list_undo = [current_str]

    last_was_undo = False
    current_str += cmd
    return current_str


def delete(cmd: str) -> str:

    n = int(cmd)

    global current_str, last_was_undo, list_undo, list_redo

    if not last_was_undo:
        list_undo.append(current_str)
    else:
        list_redo = []
        list_undo = [current_str]

    last_was_undo = False
    current_str = current_str[:-n]
    return current_str


def get(cmd: str) -> str:

    i = int(cmd)
    return current_str[
        i : i + 1
    ]  # берем срез чтобы не обрабатывать исключение


def undo(cmd: str) -> str:

    global current_str, last_was_undo

    if not list_undo:
        return current_str

    last_was_undo = True

    list_redo.append(current_str)
    current_str = list_undo.pop()
    return current_str


def redo(cmd: str) -> str:

    global current_str, last_was_undo

    if not list_redo:
        return current_str

    last_was_undo = False

    list_undo.append(current_str)
    current_str = list_redo.pop()
    return current_str


methods = [append, delete, get, undo, redo]


def BastShoe(cmd: str) -> str:

    method = methods[int(cmd[0]) - 1]
    return method(cmd[2:])
