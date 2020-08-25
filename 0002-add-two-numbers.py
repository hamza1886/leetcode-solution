# see: https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        val = l1.val + l2.val
        carry = val // 10
        ret = ListNode(val % 10)

        if l1.next is not None or l2.next is not None or carry != 0:
            if l1.next is None:
                l1.next = ListNode(0)
            if l2.next is None:
                l2.next = ListNode(0)

            l1.next.val += carry
            ret.next = self.addTwoNumbers(l1.next, l2.next)

        return ret

    def make_list_node(self, l: [int]) -> ListNode:
        ln = temp = None

        for v in l:
            if ln is None:
                ln = ListNode(v)
                temp = ln
            else:
                temp.next = ListNode(v)
                temp = temp.next

        return ln

    def print_node_list(self, ln: ListNode) -> list:
        temp = ln
        l = []

        while temp is not None:
            l.append(temp.val)
            temp = temp.next

        return l


if __name__ == '__main__':
    solution = Solution()
    ln1 = solution.make_list_node([2, 4, 3])
    ln2 = solution.make_list_node([5, 6, 4])
    sum_ln = solution.addTwoNumbers(ln1, ln2)
    l = solution.print_node_list(sum_ln)
    print(l)  # [7, 0, 8]
