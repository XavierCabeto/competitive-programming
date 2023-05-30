def fill_prefix_sum(arr, n, prefix_sum):
    prefix_sum[0] = arr[0]

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1]+arr[i]

arr = [10, 4, 16, 20]
n = len(arr)

prefix_sum = [0 for i in range(n + 1)]

fill_prefix_sum(arr, n, prefix_sum)

for i in range(n):
    print(prefix_sum[i])