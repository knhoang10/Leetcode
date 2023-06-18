# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ''
        str2 = ''
        while True:
            if (l1 != None):
                str1 = str(l1.val) + str1
                l1 = l1.next

            if (l2 != None):
                str2 = str(l2.val) + str2
                l2 = l2.next
            
            if l1 == None and l2 == None:
                break
                
        num = int(str1) + int(str2)
        str3 = str(num)
        
        rst = ListNode()
        a = rst
        for i in range(len(str3)-1,-1,-1):
            a.next = ListNode(int(str3[i]))
            a = a.next
        return rst.next