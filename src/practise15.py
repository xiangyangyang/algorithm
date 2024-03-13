def countWeightVariations(n, weights, counts):
    total_weight = sum(weights[i] * counts[i] for i in range(n))
    dp = [False] * (total_weight + 1)
    dp[0] = True

    for i in range(n):
        for j in range(total_weight, -1, -1):
            if dp[j]:
                for k in range(1, counts[i] + 1):
                    if j + k * weights[i] <= total_weight:
                        dp[j + k * weights[i]] = True
                        print(j, k, weights[i], sep=" ")

    return sum(1 for val in dp if val)

def count_weights(n, weights, counts):
    # 可称的最大重量
    total_weight = sum(weights[i] * counts[i] for i in range(n))
    dp = [False] * (total_weight + 1)
    dp[0] = True
    dp[total_weight] = True

    for i in range(n):
        for j in range(total_weight + 1):
            if dp[j]:
                for k in range(1, counts[i] + 1):
                    if j + k * weights[i] < total_weight:
                        dp[j + k * weights[i]] = True
                        print(j,k,weights[i],sep=" ")

    return sum (1 for val in dp if val)

if __name__ == '__main__':
    # 测试
    n = 2
    weights = [74, 185]
    counts = [3, 2]
    print(countWeightVariations(n, weights, counts))
    # print(count_weights(n, weights, counts))
