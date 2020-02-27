# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        
        slow_runner = head
        fast_runner = head.next

        stack = [slow_runner.val]

        print(stack)

        palindrome = True

        # Create two runners, fast and slow
        # Fast moves 2x for every move slow makes
        # So when fast hits the end of the list, slow is in the middle. 
        # Keep track of the nodes slow sees
        while fast_runner and fast_runner.next:
            fast_runner = fast_runner.next.next
            slow_runner = slow_runner.next
            stack.append(slow_runner.val)

            print(stack)

        # Slow continues through the rest of the list
        # Compare the nodes to the values popped off the stack
        while slow_runner and palindrome:          
            if slow_runner.val != stack.pop():
                palindrome = False
                print(stack)

            slow_runner = slow_runner.next
            print(stack)

        if stack:
            palindrome = False

        return palindrome

def main():
    sol = Solution()

    head = ListNode(1)
    head.next = ListNode(1)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(2)
    # head.next.next.next.next = ListNode(1)

    print(sol.isPalindrome(head))

if __name__ == "__main__":
    main()