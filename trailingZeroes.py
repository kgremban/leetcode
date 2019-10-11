from math import floor

class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeroes = 0
        i = 1

        while 5**i <= n:
            zeroes += floor(n / 5**i)
            i += 1

        return zeroes

    def trailingZeroes2(self, n: int) -> int:
        zeroes = 0

        while n > 0:
            n = floor(n/5)
            zeroes += n

        return zeroes

def main():
    sol = Solution()

    print(sol.trailingZeroes2(25))

if __name__ == "__main__":
    main()