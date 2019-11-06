class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2: 
            return 2

        nMinus2 = 1
        nMinus1 = 2
        subtotal = None 
        count = 3

        while count <= n:
            subtotal = nMinus1 + nMinus2 
            nMinus2 = nMinus1
            nMinus1 = subtotal 
            count += 1
                
        return subtotal

def main():
    sol = Solution()

    input1 = 2
    input2 = 3
    input3 = 6

    print (sol.climbStairs(input3))

if __name__ == "__main__":
    main()