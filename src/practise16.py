# 华为OD算法题-贪心歌手
# 算法题：
# 一个歌手准备从A城去B城参加演出。
# （1）按照合同，他必须在T天内赶到.
# （2）歌手途径N座城市
#
# （3） 歌手不能往回走
# （4）每两座城市之间需要的天数都可以提前获知
# （5）歌手在每座城市都可以在路边卖唱赚钱。经过调研，歌手提前获知了每座城市卖唱的收入预期：
# 如果在一座城市第一天卖唱可以赚M，后续每天的收入会减少D（第二天赚的钱是M-D，第三天是M-2D..）。如果收入减到O就不会再少了。
# （6）歌手到达后的第二天才能开始卖唱。如果今天卖过唱，第二天才能出发。
# 贪心Q的歌手最多可以赚多少钱？
#
# 输入描述：
# 第一行两个数字T和N，中间用空格隔开
# T代表总天数；
# N代表路上经过N座城市；
# O <T< 1000.0<N< 100
# 第二行N+1个数字，中间用空格隔开。代表每两座城市之间耗费的时间。其总和 <=T
# 接下来N行，每行两个数字M和D，中间用空格隔开代表每个城市的收入预期。
#
# 输出描述：
# 一个数字，代表歌手最多可以赚多少钱
#
# 输入下面数据测试
# 10 2
# 1 1 2
# 120 20
# 90 10
#
# 输出
# 540
# 跑了2个测试用例通过了，并没有用贪心算法。不会用

def max_income(T, travel_times, city_incomes):
    # 从A城到B城，途径N个城市，意味着有N+1个时间间隔。而且时间间隔是必花的时间
    total_path_day = sum(travel_times)
    if total_path_day >= T: return 0
    total_income = 0
    # 剩下可用来赚钱的时间
    total_day = T - total_path_day
    # 排序，首元素肯定收益最高
    # 另外，歌手可不可以回退，好像跟最大收益没有关系，现在只是计算出策略，并不实际走
    sort_arr(city_incomes)
    while total_day > 0:
        while city_incomes[0][0] >= city_incomes[1][0] and total_day > 0:
            total_income += city_incomes[0][0]
            city_incomes[0][0] -= city_incomes[0][1]
            total_day -= 1
        sort_arr(city_incomes)

    return total_income

def sort_arr(arr: [[]]):
    # 按收益最大的排序
    arr.sort(reverse=True)
    is_income_equal = True
    for i in range(len(arr)):
        if arr[0][0] != arr[i][0]:
            is_income_equal = False
    if is_income_equal:
        # 如果收益都相等时按收益递减值的顺序排序
        arr.sort(key=lambda x: x[1])


if __name__ == '__main__':
    # Input
    T, N = map(int, input().split())
    travel_times = list(map(int, input().split()))
    city_incomes = [list(map(int, input().split())) for _ in range(N)]

    # Output
    print(max_income(T, travel_times, city_incomes))
