def maxDepth( s: str) -> int:
    l, m = 0, 0
    for x in s:
        if x == '(':
            l += 1
        elif x == ')':
            m = max(m, l)
            l -= 1

    return m


def checkValidString(s: str) -> bool:
    left_open = 0
    for char in s:
        if char == '(' or char == '*':
            left_open += 1
        else:
            left_open -= 1
        if left_open < 0:
            return False

    right_open = 0
    for char in reversed(s):
        if char == ')' or char == '*':
            right_open += 1
        else:
            right_open -= 1
        if right_open < 0:
            return False

    return True

if __name__ == '__main__':
    # print(maxDepth("(1+(2*3)+((8)/4))+1"))
    s = "****((((((*)))*"
    print(checkValidString(s))