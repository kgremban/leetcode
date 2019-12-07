# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: 
            return False

        if not root.left and not root.right:
            return root.val == sum

        left = False
        right = False

        if root.left:
            left = self.hasPathSum(root.left, (sum - root.val))
        if root.right:
            right = self.hasPathSum(root.right, (sum - root.val))

        return left or right

def main():
    sol = Solution()

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.right = TreeNode(1)

    num = 22

    print(sol.hasPathSum(root, num))

if __name__ == "__main__":
    main()