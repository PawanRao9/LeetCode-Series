# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # stack = []

        # current = head
        # while current is not None:
        #     stack.append(current.val)
        #     current = current.next

        # current = head 
        # while current is not None:
        #     current.val = stack.pop()
        #     current = current.next
        
        # return head

        prev = None
        temp = head

        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev