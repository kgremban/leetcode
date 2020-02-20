from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # Check for empty tree
        if not root:
            return root
        
        # Create a breadth-first search queue
        tree_search = deque()
        tree_search.append(root)

        # For each node, swap its left and right children
        # Then append any children to the queue
        while tree_search:
            node = tree_search.popleft()
            temp = node.left
            node.left = node.right
            node.right = temp

            if node.left:
                tree_search.append(node.left)
            if node.right:
                tree_search.append(node.right)

        return root
        
    def invertTreeRecursive(self, root: TreeNode) -> TreeNode:
        # Check for empty tree
        if not root: 
            return root

        # For each node, swap its left and right children
        # with the inverted sub-tree on that side
        else:
            temp = root.left
            root.left = self.invertTreeRecursive(root.right)
            root.right = self.invertTreeRecursive(temp)
        
        return root

    def printTree(self, root: TreeNode) -> None: 
        reader = deque()

        reader.append(root)
        
        while reader:
            node = reader.popleft()
            print(node.val)

            if node.left:
                reader.append(node.left)
            if node.right:
                reader.append(node.right)


def main():
    sol = Solution()

    root = TreeNode(4)
    
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    
    root.left.left = TreeNode(1)
    #root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    sol.printTree(root)
    print("\n\n")

    invertedTree = sol.invertTreeRecursive(root)
    sol.printTree(invertedTree)

if __name__ == "__main__":
    main()