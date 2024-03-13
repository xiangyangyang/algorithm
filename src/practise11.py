
def sort_str(s):
    arr = list(s)
    i, j = 0, 0
    for i in range(len(arr) - 1):
        j = i + 1
        while j < len(arr):
            ti = char_type(arr[i])
            tj = char_type(arr[j])
            if ti == tj != 0:
                if arr[i] > arr[j]:
                    swap(i, j, arr)
                    j += 1
                else:
                    j += 1
            elif ti == 1 and tj == 2:
                u = ord(arr[j]) - 32
                if ord(arr[i]) > u:
                    swap(i, j, arr)
                    j += 1
                else:
                    j += 1
            elif ti == 2 and tj == 1:
                u = ord(arr[j]) + 32
                if ord(arr[i]) > u:
                    swap(i, j, arr)
                    j += 1
                else:
                    j += 1
            else:
                j += 1

    return arr


def swap(i, j, arr):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def char_type(c):
    if 'A' <= c <= 'Z':
        return 1
    elif 'a' <= c <= 'z':
        return 2
    else:
        return 0


if __name__ == '__main__':
    arr = sort_str(input())
    for x in arr:
        print(x, end='')
