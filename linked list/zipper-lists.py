# problem:https://structy.net/problems/zipper-lists
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# iterative
# n = length of list1, m = length of list2
# Time:O(min(n, m)), 因為只有iterate較短的那個linked list,其餘部分則是直接接到output的最後面
# Space:O(1)
def zipper_lists(head_1, head_2):
    current_1 = head_1.next  # important
    current_2 = head_2
    tail = head_1
    count = 0
    while current_1 is not None and current_2 is not None:
        if count % 2 == 0:
            tail.next = current_2
            current_2 = current_2.next
        else:
            tail.next = current_1
            current_1 = current_1.next
        tail = tail.next
        count += 1
    if current_1 is not None:
        tail.next = current_1
    if current_2 is not None:
        tail.next = current_2
    return head_1


# recursive
def zipper_lists_recursive(head_1, head_2):
    if head_1 is None and head_2 is None:
        return None
    if head_1 is None:
        return head_2
    if head_2 is None:
        return head_1
    next_1 = head_1.next
    next_2 = head_2.next
    head_1.next = head_2
    head_2.next = zipper_lists_recursive(next_1, next_2)
    return head_1


if __name__ == '__main__':
    a = Node("a")
    b = Node("b")
    c = Node("c")
    a.next = b
    b.next = c
    # a -> b -> c

    x = Node("x")
    y = Node("y")
    z = Node("z")
    x.next = y
    y.next = z
    # x -> y -> z

    zipper_lists(a, x)
    # a -> x -> b -> y -> c -> z
