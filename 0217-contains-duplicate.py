from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        return len(nums) != len(set(nums))

    def containsDuplicateSorting(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True

        return False

def main():
    sol = Solution()

    input1 = [1, 2, 3, 1]
    input2 = [1, 2, 3, 4]
    input3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    input4 = []

    print(sol.containsDuplicate(input4))
    print(sol.containsDuplicateSorting(input4))

if __name__ == "__main__":
    main()