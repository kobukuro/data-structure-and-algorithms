# my solution
# def can_sum(target_sum, numbers):
#     def dfs(sum, numbers, number):
#         # print(f'{sum}-{number}={sum-number}')
#         sum -= number
#         if sum == 0:
#             return True
#         if sum < 0:
#             return False
#         for num in numbers:
#             if dfs(sum, numbers, num):
#                 return True
#         return False
#
#     for number in numbers:
#         if dfs(target_sum, numbers, number):
#             return True
#     return False

# 記憶點:因為can_sum function return boolean, 所以記得加上if can_sum()判斷式
# m = target sum, n = array length
# worse case: height of tree is m(because if 1 is in the array)
# 然後每一層每一個node都會再分出n個分支
# time:O(n^m), space:O(m)
# def can_sum(target_sum, numbers):
#     if target_sum == 0:
#         return True
#     if target_sum < 0:
#         return False
#     for num in numbers:
#         remainder = target_sum - num
#         if can_sum(remainder, numbers):
#             return True
#     return False

# m = target sum, n = array length
# time:O(n*m), space:O(m)
# def can_sum(target_sum, numbers, memo=None):
#     if memo is None:
#         memo = {}
#     if target_sum in memo:
#         return memo[target_sum]
#     if target_sum == 0:
#         return True
#     if target_sum < 0:
#         return False
#     for num in numbers:
#         remainder = target_sum - num
#         if can_sum(remainder, numbers, memo):
#             memo[target_sum] = True
#             return True
#     memo[target_sum] = False
#     return False

# tabulation
# m = target sum, n = array length
# time:O(mn), space:O(m)
def can_sum(target_sum, numbers):
    table = [False] * (target_sum + 1)
    table[0] = True
    for i in range(len(table)):
        if table[i]:
            for number in numbers:
                if i + number <= target_sum:
                    table[i + number] = True
    return table[-1]


if __name__ == '__main__':
    target_sum = 7
    numbers = [2, 3]
    print(can_sum(target_sum=target_sum, numbers=numbers))  # true
    target_sum = 7
    numbers = [5, 3, 4, 7]
    print(can_sum(target_sum=target_sum, numbers=numbers))  # true
    target_sum = 7
    numbers = [2, 4]
    print(can_sum(target_sum=target_sum, numbers=numbers))  # false
    target_sum = 8
    numbers = [2, 3, 5]
    print(can_sum(target_sum=target_sum, numbers=numbers))  # true
    target_sum = 300
    numbers = [7, 14]
    print(can_sum(target_sum=target_sum, numbers=numbers))  # false
