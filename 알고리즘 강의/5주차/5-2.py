def longest_increasing_subsequence(arr):
    n = len(arr)
    if n == 0:
        return 0
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

arr1 = [10, 9, 2, 5, 3, 7, 101, 18]
print(longest_increasing_subsequence(arr1))
