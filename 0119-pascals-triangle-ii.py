from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = []
        count = 0

        while count <= rowIndex:
            row.append(1)
            index = -2

            while abs(index) < len(row):
                row[index] = row[index] + row[index - 1]
                index -= 1
            
            count += 1
        
        return row

def main():
    sol = Solution()

    print(sol.getRow(4))

if __name__ == "__main__":
    main()