# problem:https://structy.net/problems/fib
# reference:https://www.youtube.com/watch?v=oBt53YbR9Kk

# height of the tree is n (從root分出來,一邊是n-2,一邊是n-1)
# 因為樹的每一層nodes數量為2的倍數,然後樹的高度為n,所以時間複雜度為O(2^n)
# 空間複雜度為O(n),也同樣為樹的高度,因為當recursive call到達base case時, 會將element pop出來
# 所以空間複雜度不是O(2^n),而是O(n)
# Time:O(2^n), Space:O(n)
# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# use memoization(store duplicate sub problems),時間複雜度可以降到O(n)
# Time:O(n), Space:O(n)
# memo:key:n, value:return value
# def fib(n, memo=None):
#     if memo is None:
#         memo = {}
#     if n in memo:
#         return memo[n]
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
#     return memo[n]

# tabulation
# 例如當n=6時,就需要一個size為7的array,然後先將每個element初始化為0,接著把index 1的值改成1
# 並且從index 0開始,將此index的值,加到下面兩個index裡的值
# Time:O(n), Space:O(n)
def fib(n):
    if n == 0:
        return 0
    arr = [0] * (n + 1)
    arr[1] = 1
    for i in range(len(arr) - 1):
        arr[i + 1] += arr[i]
        if i != len(arr) - 2:
            arr[i + 2] += arr[i]
    return arr[-1]


if __name__ == '__main__':
    print(fib(n=50))
