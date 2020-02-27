# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Two runners trace the paths to p and q.
        # Once they diverge, return the last common node (the LCA).
        # If one of the runners reaches its node before the paths diverge,
        # then that node is the LCA
        
        p_runner = root
        q_runner = root
        LCA = None

        while p_runner == q_runner:

            # If we reach either p or q, that is the LCA
            if p_runner == p:
                return p

            if q_runner == q:
                return q

            # If not, update the LCA to the current shared node
            LCA = p_runner

            # Then progress the runners forward
            if p.val < p_runner.val:
                p_runner = p_runner.left
            else:
                p_runner = p_runner.right

            if q.val < q_runner.val:
                q_runner = q_runner.left
            else:
                q_runner = q_runner.right

        # If the paths diverged, return LCA
        return LCA

    def lowestCommonAncestorRecursive(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If p and q are both less than or greater than root, then drill down into 
        # either subtree until you find the node where they diverge

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestorRecursive(root.left, p, q)
        if p.val > root.val and q.val > root.val: 
            return self.lowestCommonAncestorRecursive(root.right, p, q)
        return root

def main():
    sol = Solution()

    root = TreeNode(6)

    root.left = TreeNode(2)
    root.right = TreeNode(8)

    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    p = root.left
    q = root.left.right

    LCA = sol.lowestCommonAncestor(root, p, q)
    print(LCA.val)
    LCA_r = sol. lowestCommonAncestorRecursive(root, p, q)
    print(LCA_r.val)

if __name__ == "__main__":
    main()