
def zip_string(input_string):
    result = input_string[0]
    count = 1
    for char in input_string[1:]:
        if result[-1] == char:
            count += 1
        else:
            result += str(count)
            result += char
            count = 1
    result += str(count)
    return result


BRACES = {'(': ')', '[': ']', '{': '}'}
def group_check(s):
    stack = []
    for b in s:
        c = BRACES.get(b)
        if c:
            stack.append(c)
        elif not stack or stack.pop() != b:
            return False
    return not stack


def earthworm(array):
    a = []
    while array:
        a.extend(list(array.pop(0)))
        array = list(zip(*array))
        array.reverse()
    return a


def my_earhworm(array):
    if len(array) == 1 and len(array[0]) == 0:
        return []
    res = []
    result_pos = []
    current_pos = "00"
    direction = "e"
    result_pos.append(current_pos)
    while current_pos is not None:
        y = int(current_pos[0])
        x = int(current_pos[1])
        res.append(array[y][x])
        current_pos, direction = get_next_pos(array, current_pos, result_pos, direction)
        result_pos.append(current_pos)
    return res


def get_next_pos(_array, _current_pos, _result_pos, _direction):
    y = int(_current_pos[0])
    x = int(_current_pos[1])

    h = len(_array)
    w = len(_array[0])

    if _direction == "e":
        if x + 1 < w:  # east
            if is_valid_pos(_array, x + 1, y) and is_new_pos(_result_pos, x + 1, y):
                x += 1
                return str(y) + str(x), "e"
        if y + 1 < h:  # south
            if is_valid_pos(_array, x, y + 1) and is_new_pos(_result_pos, x, y + 1):
                y += 1
                return str(y) + str(x), "s"

    if _direction == "w":
        if x > 0:  # west
            if is_valid_pos(_array, x - 1, y) and is_new_pos(_result_pos, x - 1, y):
                x -= 1
                return str(y) + str(x), "w"
        if y > 0:  # north
            if is_valid_pos(_array, x, y - 1) and is_new_pos(_result_pos, x, y - 1):
                y -= 1
                return str(y) + str(x), "n"

    if _direction == "s":
        if y + 1 < h:  # south
            if is_valid_pos(_array, x, y + 1) and is_new_pos(_result_pos, x, y + 1):
                y += 1
                return str(y) + str(x), "s"
        if x > 0:  # west
            if is_valid_pos(_array, x - 1, y) and is_new_pos(_result_pos, x - 1, y):
                x -= 1
                return str(y) + str(x), "w"

    if _direction == "n":
        if y > 0:  # north
            if is_valid_pos(_array, x, y - 1) and is_new_pos(_result_pos, x, y - 1):
                y -= 1
                return str(y) + str(x), "n"
        if x + 1 < w:  # east
            if is_valid_pos(_array, x + 1, y) and is_new_pos(_result_pos, x + 1, y):
                x += 1
                return str(y) + str(x), "e"

    return None, None


def is_valid_pos(_array, _x, _y):
    try:
        v = _array[_x][_y]
        return True
    except Exception as e:
        return False


def is_new_pos(_result_pos, _x, _y):
    return str(_y) + str(_x) not in _result_pos