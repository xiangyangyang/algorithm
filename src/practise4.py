def jump_floor(numbers):
    if numbers <= 2:
        return numbers

    prev_prev_step = 1
    prev_step = 2
    current_step = 0

    for i in range(3, numbers + 1):
        current_step = prev_prev_step + prev_step
        prev_prev_step = prev_step
        prev_step = current_step

    return current_step


def move_xy(llist: []):
    x = 0
    y = 0
    for xy in llist:
        f = xy[:2]
        value = int(xy[1:])

        if f == 'A':
            x = x - value
        elif f == 'D':
            x = x + value
        elif f == 'W':
            y = y + value
        elif f == 'S':
            y = y - value

    return x, y


def is_valid_password(password):
    # 长度超过8位
    if len(password) < 8: return False
    # 包括大小写字母.数字.其它符号,以上四种至少三种
    # 代表含有数字，大写字母，小写字母，其它符号
    categories = [0, 0, 0, 0]
    for char in password:
        if '0' <= char <= '9':
            categories[0] = 1
        elif 'A' <= char <= 'Z':
            categories[1] = 1
        elif 'a' <= char <= 'z':
            categories[2] = 1
        elif not (char == '\n' and char == ' '):
            categories[3] = 1
    if sum(categories) < 3:
        return False

    # 不能有长度大于2的包含公共元素的子串重复
    for i in range(len(password) - 2):
        if password.count(password[i:i + 3]) > 1:
            return False

    return True

if __name__ == "__main__":
    # print(jump_floor(35))
    s = input()
    # llist = s.split(';')
    # print(move_xy(llist))

    result = "OK" if is_valid_password(s) else "NG"
    print(result)