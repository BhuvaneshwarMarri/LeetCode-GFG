# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums=set(nums)
        temp=ListNode(-1)
        htemp=temp
        temp_var=head
        while temp_var is not None:
            if temp_var.val not in nums:
                temp.next=temp_var
                temp=temp.next
            temp_var=temp_var.next
        temp.next=None
        return htemp.next
            
        