# region my solution
# def how_sum(target_sum, numbers):
#     res = []
#
#     def dfs(target_sum, numbers, path):
#         if target_sum == 0:
#             res.append(path)
#             return True
#         if target_sum < 0:
#             return False
#         for number in numbers:
#             remainder = target_sum - number
#             if dfs(remainder, numbers, path + [number]):
#                 return True
#         return False
#
#     if dfs(target_sum, numbers, []):
#         return res[0]
#     return None


# endregion

# region Brute force solution
# m = target sum, n = array length
# Time:O(n^m * m), Space:O(m)
def how_sum(target_sum, numbers):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for number in numbers:
        remainder = target_sum - number
        remainder_result = how_sum(remainder, numbers)
        if remainder_result is not None:
            return [*remainder_result, number]
    return None


# endregion

# region memoization solution
# Time:O(n*m*m), Space:O(m^2)
# def how_sum(target_sum, numbers, memo=None):
#     if memo is None:
#         memo = {}
#     if target_sum in memo:
#         return memo[target_sum]
#     if target_sum == 0:
#         return []
#     if target_sum < 0:
#         return None
#     for number in numbers:
#         remainder = target_sum - number
#         remainder_result = how_sum(remainder, numbers, memo)
#         if remainder_result is not None:
#             memo[target_sum] = [*remainder_result, number]
#             return memo[target_sum]
#     memo[target_sum] = None
#     return memo[target_sum]


# endregion

# region tabulation
# m = target sum, n = array length
# Time:O(m*n*m), Space:O(m^2)
# def how_sum(target_sum, numbers):
#     table = [None] * (target_sum + 1)
#     table[0] = []
#     # print(table)
#     for i in range(len(table)):
#         for number in numbers:
#             if table[i] is not None:
#                 if i + number <= len(table) - 1:
#                     table[i + number] = table[i] + [number]
#                     if i + number == len(table) - 1:
#                         return table[-1]
#     return None


# endregion

if __name__ == '__main__':
    target_sum = 7
    numbers = [2, 3]
    print(how_sum(target_sum=target_sum, numbers=numbers))  # true
    target_sum = 7
    numbers = [5, 3, 4, 7]
    print(how_sum(target_sum=target_sum, numbers=numbers))  # true
    target_sum = 7
    numbers = [2, 4]
    print(how_sum(target_sum=target_sum, numbers=numbers))  # false
    target_sum = 8
    numbers = [2, 3, 5]
    print(how_sum(target_sum=target_sum, numbers=numbers))  # true
    target_sum = 300
    numbers = [7, 14]
    print(how_sum(target_sum=target_sum, numbers=numbers))  # false
