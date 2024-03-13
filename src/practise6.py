import sys


def ip_to_int(ip):
    # 拆分IP地址
    ip_parts = ip.split('.')

    # 将每个部分转换为二进制并连接起来
    binary_str = ''
    for part in ip_parts:
        binary_str += format(int(part), '08b')  # '08b'表示将整数转换为8位二进制数

    # 将二进制字符串转换为长整数
    print(binary_str)
    print(type(binary_str))
    return int(binary_str, 2)


def int_to_ip(num):
    # 将长整数转换为32位二进制字符串
    binary_str = format(num, '032b')

    # 将二进制字符串拆分为四个部分
    parts = [binary_str[i:i + 8] for i in range(0, 32, 8)]

    # 将每个部分转换回十进制数并连接成IP地址字符串
    ip_address = '.'.join(str(int(part, 2)) for part in parts)

    return ip_address


def ip_to_int1(ip):
    # 拆分IP地址
    ip_parts = ip.split('.')

    # 将每个部分转换为二进制并连接起来
    binary_str = ((int(ip_parts[0]) << 24) + (int(ip_parts[1]) << 16) +
                  (int(ip_parts[2]) << 8) + int(ip_parts[3]))

    # 将二进制字符串转换为长整数
    return binary_str


def int_to_ip1(num):
    parts = [num >> 24, (num >> 16)&0xff, (num >>8) & 0xff, num&0xff]
    parts.sort(reverse=True)


    # 将每个部分转换回十进制数并连接成IP地址字符串
    ip_address = '.'.join(str(part) for part in parts)

    return ip_address


if __name__ == '__main__':
    # 测试
    # ip_address = "10.3.3.193"
    # result = ip_to_int(ip_address)
    # print("IP地址转换后的长整数为:", result)
    #
    # ip_number = 167969729
    # print("整数转换后的IP地址为:",int_to_ip(ip_number))
    ip = input()
    num = int(input())
    print(ip_to_int1(ip))
    print(int_to_ip1(num))
