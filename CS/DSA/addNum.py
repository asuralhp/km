# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next




#flipped first, flip back later
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        listl1 = []
        listl2 = []
        while True:
            if l1 != None:
                listl1.append(l1.val)
                l1 = l1.next
            
            if l2 != None:
                listl2.append(l2.val)
                l2 = l2.next
            if l1 == None and l2 == None :
                break
        l3_total = int(''.join(map(str,listl1[::-1]))) + int(''.join(map(str,listl2[::-1])))
        l3 = ListNode()
        l = l3
        listl3 = list(map(int, str(l3_total)))[::-1]
        for n, i in enumerate(listl3):
            l.val = i
            if n < len(listl3) - 1:
                l.next = ListNode()
                l = l.next
        return l3

        
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result