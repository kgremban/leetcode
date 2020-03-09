class Solution:
    def isUgly(self, num: int) -> bool:
        
        # Check base case, where num is 0 or negative
        if num <= 0:
            return False
        
        # Keep dividing num by ugly factors until it either
        # equals 1 (ugly = True) or can't be divided anymore
        # (ugly = False)
        for x in [2, 3, 5]:
            while num % x == 0:
                num = num / x

        return num == 1

def main():
    sol = Solution()

    print(sol.isUgly(112))

if __name__ == "__main__":
    main()