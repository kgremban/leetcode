from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Reject base case with no duplicates
        if len(nums) == len( set(nums) ):
            return False

        # Scan through list
        for i in range(len(nums)):
            # Check rolling window of k items
            for j in range( i+1, i+k+1 ):
                # Skip edge case where window overshoots list
                if j >= len(nums):
                    continue

                # Check if duplicate is in window
                elif nums[i] == nums[j]:
                    return True

        # No nearby duplicates found
        return False

def main():
    sol = Solution()

    nums1 = [1, 2, 3, 1]
    nums2 = [1, 0, 1, 1]
    nums3 = [1, 2, 3, 1, 2, 3]

    print(sol.containsNearbyDuplicate(nums2, 1))

if __name__ == "__main__":
    main()