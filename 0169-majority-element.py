from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()       
        return nums[len(nums) // 2]

def main():
    sol = Solution()

    input1 = [3, 2, 3]
    input2 = [2, 2, 1, 1, 1, 2, 2]

    print(sol.majorityElement(input2))

if __name__ == "__main__":
    main()