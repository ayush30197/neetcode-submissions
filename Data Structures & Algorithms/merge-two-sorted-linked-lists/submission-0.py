# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            result_list_head = result_list_tail = list1
            list1 = list1.next
        else:
            result_list_head =  result_list_tail = list2
            list2 = list2.next


        while list1 and list2:
            if list1.val <= list2.val:
                print("append list 1 value and move next")
                new_node = list1
                list1 = list1.next
            else:
                print("append list 2 value and move next")
                new_node = list2
                list2 = list2.next

            result_list_tail.next = new_node
            result_list_tail = new_node

        if list1:
            result_list_tail.next = list1

        if list2:
            result_list_tail.next = list2

        return result_list_head