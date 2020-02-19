# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        else:
            leftDepth = self.maxDepth(root.left)
            rightDepth = self.maxDepth(root.right)

            return max(leftDepth, rightDepth) + 1

def main():
    sol = Solution()

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(0)


    print(sol.maxDepth(root))

if __name__ == "__main__":
    main()