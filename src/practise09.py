"""
1.遍历输入的法则字符串，当遇到一个大写字母时，表示这是一个矩阵。我们将其入栈。
2.当遇到左括号时，我们将其入栈。
3.当遇到右括号时，表示可以计算矩阵乘法了。此时我们从栈中弹出两个矩阵，并进行乘法运算，然后将结果入栈。
4.重复步骤1到3，直到遍历完整个法则字符串。
5.最终栈中只会剩下一个矩阵，即最终的结果
这种迭代的计算，渐渐减少，也要考虑栈
"""

if __name__ == '__main__':
    while True:
        try:
            # 矩阵个数，输入的字符与所代表的矩阵的映射{A:[20 30]}，计算输入串的栈，计算结果
            n, dict, stack, res = int(input()), {}, [], 0
            for i in range(n):
                key = chr(ord('A') + i)
                dict[key] = list(map(int, input().strip().split()))
            print(dict)
            
            # 输入的计算字符串
            s = input()
            for char in s:
                if char != ')':
                    stack.append(char)
                else:
                    n, m = stack.pop(), stack.pop()
                    # 弹出左括号
                    stack.pop()
                    res += dict[m][0] * dict[m][1] * dict[n][1]
                    # 计算结果字符押回栈并更新字典值
                    stack.append(m)
                    dict[m] = [dict[m][0], dict[n][1]]

            print(res)
        except:
            break
