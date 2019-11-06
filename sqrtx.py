class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        mid = (high + low) // 2

        while low <= high: 
            # Perfect square
            if mid * mid == x:
                return mid

            # Mid squared is too high
            if mid * mid > x:
                high = mid - 1
                mid = (high + low) // 2

            # Mid squared is too low
            else:
                low = mid + 1
                mid = (high + low) // 2

        return mid

def main():
    sol = Solution()

    input1 = 4
    input2 = 8
    input3 = 1

    print(sol.mySqrt(input3))

if __name__ == "__main__":
    main()