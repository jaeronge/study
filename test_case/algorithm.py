
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