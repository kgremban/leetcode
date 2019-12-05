from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: 
            return None

        else:
            mid = (len(nums) - 1) // 2
            node = TreeNode(nums[mid])
            node.left = self.sortedArrayToBST(nums[:mid])
            node.right = self.sortedArrayToBST(nums[(mid + 1):])
            return node

def main():
    sol = Solution()

    nums = [-10,-3,0,5,9]

    print(sol.sortedArrayToBST(nums))

if __name__ == "__main__":
    main()