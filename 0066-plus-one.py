from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        index = len(digits) - 1

        while index >= 0:
            if digits[index] == 9:
                digits[index] = 0
                index -= 1
            else:
                digits[index] += 1
                return digits
        
        return [1] + digits

def main():

    sol = Solution()

    input1 = [1, 2, 3]
    input2 = [4, 3, 2, 1]
    input3 = [1, 9, 9, 9]

    print(sol.plusOne(input3))

if __name__ == "__main__":
    main()