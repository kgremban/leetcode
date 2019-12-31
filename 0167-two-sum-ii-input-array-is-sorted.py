from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        
        while index1 < len(numbers):

            if numbers[index1] == numbers[index1 - 1]:
                index1 += 1
                continue

            index2 = index1 + 1
            while index2 < len(numbers) and (numbers[index1] + numbers[index2]) <= target:
                if numbers[index1] + numbers[index2] == target:
                    return [index1 + 1, index2 + 1]
                else:
                    index2 += 1
            index1 += 1
        return []

    def twoSumInverse(self, numbers: List[int], target: int) -> List[int]:
        lowIndex = 0
        highIndex = len(numbers) - 1

        while lowIndex < highIndex:
            if numbers[lowIndex] + numbers[highIndex] == target:
                return [lowIndex + 1, highIndex + 1]
            if numbers[lowIndex] + numbers[highIndex] < target:
                lowIndex += 1
            if numbers[lowIndex] + numbers[highIndex] > target:
                highIndex -= 1


def main():
    sol = Solution()

    numbers = [2, 7, 7, 11, 15]
    target = 14

    print(sol.twoSumInverse(numbers, target))

if __name__ == "__main__":
    main()