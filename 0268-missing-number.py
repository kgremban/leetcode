from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Sort nums
        nums.sort()
        
        # Verify that 0 is the first item, else 0 is missing
        if nums[0] != 0:
            return 0

        # Iterate through the list, and return the missing number
        for i in range(len(nums) - 1):
            if (nums[i] + 1) == nums[i+1]:
                continue
            else:
                return (nums[i] + 1)

        # If no number is missing, it's the last number + 1
        return nums[-1] + 1

def main():
    sol = Solution()

    input1 = [3, 0, 1]
    input2 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    input3 = []

    print(sol.missingNumber(input1))
    print(sol.missingNumber(input2))

if __name__ == "__main__":
    main()