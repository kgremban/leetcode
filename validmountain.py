from typing import List

class Solution: 
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False

        isMount = False
        i = 0

        while i < (len(A) - 2):
            if (A[i] == A[i+1]):
                return False

            elif (A[i] > A[i+1]) and (A[i+1] < A[i+2]):
                return False

            elif (A[i] < A[i+1] and (A[i+1] > A[i+2])):
                isMount = True
            
            i += 1

        return isMount


def main():

    #input = [0, 3, 2, 1]
    input = [0, 1, 5, 4, 3, 2, 3]
    #input = [0, 0, 1, 0]

    sol = Solution()
    print(sol.validMountainArray(input))

if __name__ == "__main__":
    main()
