# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        if headA == headB:
            return headA

        nextA = (headA.next != None)
        nextB = (headB.next != None)

        visitedA = []
        visitedB = []
        
        while nextA or nextB:

            visitedA.append(headA)
            visitedB.append(headB)

            if headA in visitedB:
                return headA

            if headB in visitedA:
                return headB

            if headA.next:
                headA = headA.next
            else: 
                nextA = False

            if headB.next:
                headB = headB.next
            else:
                nextB = False

        return None

def main():
    sol = Solution()

    a1 = ListNode(4)
    a2 = ListNode(1)

    b1 = ListNode(5)
    b2 = ListNode(0)
    b3 = ListNode(1)

    c1 = ListNode(8)
    c2 = ListNode(4)
    c3 = ListNode(5)

    a1.next = a2
    a2.next = c1

    b1.next = b2
    b2.next = b3
    b3.next = c1

    c1.next = c2
    c2.next = c3

    d1 = ListNode(3)
    e1 = ListNode(2)
    e1.next = d1

    print(sol.getIntersectionNode(a1, b1))

if __name__ == "__main__":
    main()