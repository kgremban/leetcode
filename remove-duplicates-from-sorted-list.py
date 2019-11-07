# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head

        tail = False
        pointer1 = head
        pointer2 = head.next

        while not tail:
            if pointer1.val == pointer2.val:
                if pointer2.next:
                    pointer2 = pointer2.next
                else: 
                    pointer1.next = None
                    tail = True    
            else:
                pointer1.next = pointer2

                if pointer2.next:
                    pointer1 = pointer1.next
                    pointer2 = pointer2.next
                else: 
                    tail = True

        return head


def printLinkedList(node):
    print(node.val)
    if node.next:
        printLinkedList(node.next)

def main():
    sol = Solution()

    # Example 2
    head = ListNode(1)
    
    n1 = ListNode(1)
    head.next = n1

    n2 = ListNode(2)
    n1.next = n2
    
    n3 = ListNode(3)
    n2.next = n3

    n4 = ListNode(3)
    n3.next = n4

    # Test cases
    head2 = ListNode(1)

    printLinkedList(sol.deleteDuplicates(head2))

if __name__ == "__main__":
    main()
