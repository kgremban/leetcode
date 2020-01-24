from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p:
            if q:
                return False
            if not q: return True

        if not q:
            return False

        search_p = deque()
        search_p.append(p)
        
        search_q = deque()
        search_q.append(q)

        while search_p and search_q:
            check_p = search_p.popleft()
            check_q = search_q.popleft()

            if check_p.val != check_q.val:
                return False

            else:
                # If both nodes have a left node, add them to queues
                if check_p.left and check_q.left:
                    search_p.append(check_p.left)
                    search_q.append(check_q.left)
                # If one node has a left node, but the other doesn't
                # Trees are not the same
                elif check_p.left != check_q.left:
                    return False

                # Ditto right nodes
                if check_p.right and check_q.right:
                    search_p.append(check_p.right)
                    search_q.append(check_q.right)
                elif check_p.right != check_q.right:
                    return False

        return True

def main():

    sol = Solution()

    p_head = TreeNode(1)
    p_left = TreeNode(2)
    p_right = TreeNode(3)

    p_head.left = p_left
    p_head.right = p_right

    q_head = TreeNode(1)
    q_left = TreeNode(2)
    q_right = TreeNode(2)

    q_head.left = q_left
    q_head.right = q_right

    null_head = TreeNode(None)

    print(sol.isSameTree(null_head, null_head))

if __name__ == "__main__":
    main()