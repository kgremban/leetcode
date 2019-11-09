from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        countM = m - 1
        countN = n - 1
        index = m + n - 1

        while countM >= 0 and countN >= 0:
            if nums1[countM] >= nums2[countN]:
                nums1[index] = nums1[countM]
                index -= 1
                countM -= 1
            else:
                nums1[index] = nums2[countN]
                index -= 1
                countN -= 1

        while countN >= 0:
            nums1[index] = nums2[countN]
            index -= 1
            countN -= 1
        
def main():
    sol = Solution()

    nums1 = [0, 0, 0, 0, 0, 0]
    m = 0
    nums2 = [1, 3, 6, 9]
    n = 4

    sol.merge(nums1, m, nums2, n)

    print(nums1)

if __name__ == "__main__":
    main()