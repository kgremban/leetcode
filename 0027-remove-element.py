from typing import List

class Solution:
    def removeElement1(self, nums: List[int], val: int) -> int:
        
        while val in nums:
            nums.remove(val)
        
        return len(nums)

    def removeElement2(self, nums: List[int], val: int) -> int:

        i = 0

        while i < len(nums):

            if nums[-1] == val:
                nums.pop()

            elif nums[i] == val:
                nums[i] = nums[-1]
                nums.pop()
                i += 1
            
            else: i += 1

        return len(nums)

def main(): 
    sol = Solution()

    nums1 = [3,2,2,3]
    val1 = 3

    nums2 = [0,1,2,2,3,0,4,2]
    val2 = 2

    nums3 = [0]
    val3 = 0

    print(sol.removeElement2(nums3, val3))
    print(nums3)

if __name__ == "__main__":
    main()