# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        behind = None

        while head.next:
            # Don't lose the next node
            ahead = head.next
            
            # Point head backwards
            head.next = behind
            
            # Progress forward in the list
            behind = head
            head = ahead

        head.next = behind
        return head

    def printLinkedList(self, head: ListNode) -> None:
        while True:
            print(head.val)
            if head.next:
                head = head.next
            else:
                return

def main():
    sol = Solution()

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    reversed = sol.reverseList(head)
    sol.printLinkedList(reversed)

if __name__ == "__main__":
    main()

