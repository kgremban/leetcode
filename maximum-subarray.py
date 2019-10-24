from typing import List

class Solution:
    def maxSubArray_tooSlow(self, nums: List[int]) -> int:
        max = nums[0]  
        pointer1 = 0

        while pointer1 < len(nums):
            pointer2 = pointer1 + 1

            while pointer2 <= len(nums):
                if sum(nums[pointer1:pointer2]) > max:
                    max = sum(nums[pointer1:pointer2])
                pointer2 += 1
            
            pointer1 += 1

        return max

    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        max = sum(nums[:])



        return max

def main():
    sol = Solution()

    input1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    input2 = [-5, -3, -1, 1, 3, 5]
    input3 = [-1]

    print(sol.maxSubArray(input3))

if __name__ == "__main__":
    main()