# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        # Base case
        if not head.next:
            if head.val == val:
                return None
            
        # Move the head forward to the first non-val node
        while head.val == val:
            if head.next:
                head = head.next
            else:
                return None

        # Scan through the linked list
        runner = head
        while runner.next:

            # If the next node contains val, see if there's a
            # next next node to point to, otherwise end the list
            if runner.next.val == val:
                if runner.next.next:
                    runner.next = runner.next.next

                else:
                    runner.next = None

            # If the next node doesn't contain val, move forward
            else: runner = runner.next

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

    head = ListNode(6)
    head.next = ListNode(2)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = ListNode(6)

    output = sol.removeElements(head, 6)
    sol.printLinkedList(output)

if __name__ == "__main__":
    main()