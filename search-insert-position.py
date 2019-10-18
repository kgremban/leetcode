from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if not nums:
            return 0

        if target < nums[0]: 
            return 0

        if target > nums[-1]:
            return len(nums)

        low = 0
        high = len(nums) -1
        foundTarget = False

        while not foundTarget:

            index = (low + high) // 2

            if nums[index] == target:
                foundTarget = True

            elif nums[index] > target:
                if nums[index - 1] < target:
                    foundTarget = True

                else: 
                    high = index - 1

            else: 
                if nums [index + 1] > target:
                    index += 1
                    foundTarget = True
                
                else:
                    low = index + 1

        return index

    def searchInsert2(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)

        while low < high:
            index = (low + high) // 2

            if target > nums[index]:
                low = index + 1
            else: 
                high = index

        return low

def main():
    sol = Solution()

    nums1 = [1, 3, 5, 6, 7]
    nums2 = [4, 5, 7, 9, 10, 12, 13, 17, 22, 45, 57, 80]
    nums3 = [1, 3, 5]
    nums4 = [1, 4, 6, 7, 8, 9]
    nums5 = []

    target1 = 5
    target2 = 2
    target3 = 7
    target4 = 0
    target5 = 50
    target6 = 6

    print(sol.searchInsert2(nums3, target1))

if __name__ == "__main__":
    main()