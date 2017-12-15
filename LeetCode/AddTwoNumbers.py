# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first_integer = ""
        second_integer = ""
        root_node = ListNode(0)
        node = root_node

        while l1 != None:
            first_integer = str(l1.val) + first_integer
            l1 = l1.next

        while l2 != None:
            second_integer = str(l2.val) + second_integer
            l2 = l2.next

        sum = int(first_integer) + int(second_integer)

        if sum == 0:
            rem = sum % 10
            node.next = ListNode(rem)
            node = node.next

        while sum > 0:
            rem = sum % 10
            node.next = ListNode(rem)
            node = node.next
            sum = sum / 10

        return root_node.next
