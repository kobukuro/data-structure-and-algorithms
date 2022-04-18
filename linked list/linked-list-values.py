# problem:https://structy.net/problems/linked-list-values
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# n = number of nodes
# Time:O(n), Space:O(n)
# iterative
# def linked_list_values(head):
#     res = []
#     curr = head
#     while curr is not None:
#         res.append(curr.val)
#         curr = curr.next
#     return res

# recursive
def linked_list_values(head):
    res = []

    def helper(curr):
        if curr is None:
            return
        res.append(curr.val)
        helper(curr.next)

    helper(head)
    return res


if __name__ == '__main__':
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d
    print(linked_list_values(head=a))
