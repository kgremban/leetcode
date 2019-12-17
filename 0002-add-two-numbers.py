# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        sum = l1.val + l2.val
        
        if sum < 10:
            head = ListNode(sum)
            carry = False
        else: 
            head = ListNode(sum % 10)
            carry = True

        pointer = head

        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next

            sum = l1.val + l2.val

            if carry: 
                sum += 1

            if sum < 10:
                newNode = ListNode(sum)
                carry = False
            else: 
                newNode = ListNode(sum % 10)
                carry = True

            pointer.next = newNode
            pointer = pointer.next

        while l1.next:
            if not carry:
                pointer.next = l1.next
                break
            else:
                l1 = l1.next
                sum = l1.val + 1

                if sum < 10:
                    newNode = ListNode(sum)
                    carry = False
                else: 
                    newNode = ListNode(sum % 10)
                    carry = True

                pointer.next = newNode
                pointer = pointer.next

        while l2.next:
            if not carry:
                pointer.next = l2.next
                break
            else:
                l2 = l2.next
                sum = l2.val + 1

                if sum < 10:
                    newNode = ListNode(sum)
                    carry = False
                else: 
                    newNode = ListNode(sum % 10)
                    carry = True

                pointer.next = newNode
                pointer = pointer.next

        if carry:
            newNode = ListNode(1)
            pointer.next = newNode

        return head

def printLinkedList(node: ListNode) -> None:
    print(node.val)
    if node.next:
        printLinkedList(node.next)

def main():
    sol = Solution()

    list1_head = ListNode(2)
    list1_node1 = ListNode(4)
    list1_node2 = ListNode(3)
    list1_node3 = ListNode(2)

    list1_head.next = list1_node1
    list1_node1.next = list1_node2
    list1_node2.next = list1_node3

    list2_head = ListNode(5)
    list2_node1 = ListNode(6)
    list2_node2 = ListNode(4)
    list2_node3 = ListNode(8)

    list2_head.next = list2_node1
    list2_node1.next = list2_node2
    list2_node2.next = list2_node3

    printLinkedList(sol.addTwoNumbers(list1_head, list2_head))

if __name__ == "__main__":
    main()

