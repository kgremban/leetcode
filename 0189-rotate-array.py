from typing import List

class Solution:

    def rotateB(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = nums[:len(nums)-k]
        del nums[:len(nums)-k]
        nums.extend(temp)

    def rotateA(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = 0

        while count < k:
            tmp = nums.pop()
            nums.insert(0, tmp)
            count += 1

        print(nums)


def main():
    sol = Solution()

    input1 = [1, 2, 3, 4, 5, 6, 7]
    input2 = [-1, -100, 3, 99]

    sol.rotateB(input1, 3)

    print(input1)

if __name__ == "__main__":
    main()