class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if (x < 0):
            return False

        xstr = str(x)
        xstr_reversed = xstr[::-1]

        if (xstr == xstr_reversed):
            return True

        return False

def main(): 
    sol = Solution()

    input1 = 121
    input2 = -121
    input3 = 10000
    input4 = 4

    print(sol.isPalindrome(input4))

if __name__ == "__main__":
    main()