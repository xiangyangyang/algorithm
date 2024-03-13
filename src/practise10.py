if __name__ == '__main__':
    n, dic = int(input()), {}
    for i in range(n):
        chars = input().split()
        key = int(chars[0])
        value = int(chars[1])
        if key in dic.keys():
            dic[key] = dic[key] + value
        else:
            dic[key] = value

    new_dic = sorted(dic.items())
    for k, v in new_dic:
        print(k, v)