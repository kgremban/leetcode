from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)
        
        maxLoot = [0 for i in range(len(nums))]
        maxLoot[0] = nums[0]
        maxLoot[1] = max(nums[0], nums[1])

        # For each index, see if adding it to maxLoot[index-2] 
        # lands a better haul than skipping it and taking
        # maxLoot[index-1]
        for i in range(2, len(nums)):
            maxLoot[i] = max((maxLoot[i-2] + nums[i]), maxLoot[i-1])

        return maxLoot[-1]

def main():
    sol = Solution()

    input1 = [1, 2, 3, 1]
    input2 = [2, 7, 9, 3, 1]
    input3 = [2, 1, 1, 2]

    print(sol.rob(input3))

if __name__ == "__main__":
    main()