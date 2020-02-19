from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        row = 0

        while row < numRows:
            triangle.append([0 for i in range(row + 1)])
            triangle[row][0] = 1
            triangle[row][-1] = 1

            column = 1

            while column < (row):
                triangle[row][column] = triangle[row - 1][column - 1] + triangle[row - 1][column]
                column += 1

            row += 1

        return triangle

def main():
    sol = Solution()

    print(sol.generate(5))

if __name__ == "__main__":
    main()
