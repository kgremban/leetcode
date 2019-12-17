# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        cycle = False

        slowPointer = head
        fastPointer = head

        while not cycle and slowPointer.next and fastPointer.next and fastPointer.next.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

            if slowPointer == fastPointer:
                cycle = True

        return cycle

def main():
    sol = Solution()

    head1 = ListNode(3)
    head1.next = ListNode(2)
    head1.next.next = ListNode(0)
    head1.next.next.next = ListNode(-4)
    head1.next.next.next.next = head1.next

    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = head2

    head3 = ListNode(1)

    print(sol.hasCycle(head1))

if __name__ == "__main__":
    main()