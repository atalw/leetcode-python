```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        root = pointer = ListNode(0)
        
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    pointer.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    pointer.next = ListNode(l2.val)
                    l2 = l2.next
            else:
                if l1:
                    pointer.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    pointer.next = ListNode(l2.val)
                    l2 = l2.next
                    
            pointer = pointer.next
        
        return root.next
```
