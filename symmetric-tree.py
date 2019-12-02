from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if not root:
            return True
        if root.left == None and root.right == None:
            return True
        if root.left == None or root.right == None:
            return False

        leftToRight = deque()
        leftToRight.append(root)
        leftToRightVals = [root.val]

        rightToLeft = deque()
        rightToLeft.append(root)
        rightToLeftVals = [root.val]

        while leftToRight and rightToLeft and (leftToRightVals == rightToLeftVals):
            LTR = leftToRight.popleft()
            if LTR.left:
                leftToRight.append(LTR.left)
                leftToRightVals = leftToRightVals + [LTR.left.val]
            else:
                leftToRightVals = leftToRightVals + ["null"]

            if LTR.right:
                leftToRight.append(LTR.right)
                leftToRightVals = leftToRightVals + [LTR.right.val]
            else:
                leftToRightVals = leftToRightVals + ["null"]

            RTL = rightToLeft.popleft()
            if RTL.right:
                rightToLeft.append(RTL.right)
                rightToLeftVals = rightToLeftVals + [RTL.right.val]
            else:
                rightToLeftVals = rightToLeftVals + ["null"]

            if RTL.left:
                rightToLeft.append(RTL.left)
                rightToLeftVals = rightToLeftVals + [RTL.left.val]
            else:
                rightToLeftVals = rightToLeftVals + ["null"]

        if not rightToLeft and not leftToRight and (rightToLeftVals == leftToRightVals):
            return True

        return False
                

def main():
    sol = Solution()

    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(4)
    node6 = TreeNode(3)

    root.left = node1
    root.right = node2

    node1.left = node3
    node1.right = node4

    #node2.left = node5
    node2.right = node6

    print(sol.isSymmetric(root))

if __name__ == "__main__":
    main()