class Solution:
    def reverse(self, x: int) -> int:
        if x < (-2 ** 31) or x > (2 ** 31 - 1):
            return 0
        if x >= 0:
            integer = str(x)
            reverseInt = int(integer[::-1])
            if reverseInt > (2 ** 31 - 1):
                return 0
            return reverseInt
        integer = str(abs(x))
        reverseInt = int(integer[::-1])
        if reverseInt > (2 ** 31):
                return 0
        return int(reverseInt) * -1

def main():
    integer = -15342
    sol = Solution()
    print(sol.reverse(integer))

if __name__ == "__main__":
    main()