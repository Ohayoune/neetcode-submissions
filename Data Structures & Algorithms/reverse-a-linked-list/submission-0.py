# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start_head = head #The node at the start that becomes the last node
        first_node = head #The first node in the new sequence

        #Make sure the array is not empty
        if start_head is None:
            return first_node
        
        while start_head.next is not None:
            s_h_n = start_head.next
            start_head.next = start_head.next.next
            s_h_n.next = first_node
            first_node = s_h_n
            
        return first_node

# 1 -> 2 - > 3 -> 4
# 2 -> 1 -> 3 -> 4 
# 3 -> 2 -> 1 -> 4
# 4 -> 3 -> 2 -> 1
# For every step you need to store:
    #The first_node, the start_head, what the s_h_n points to.
    #in each step,
        #start_head points to the next.next.node
        #s_h_n points to the first node and becomes the new first node



        