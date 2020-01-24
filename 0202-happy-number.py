class Solution:
    def isHappy(self, n: int) -> bool:
        checked = []
        happySum = n

        while happySum != 1:
            n = happySum
            happySum = 0

            while n:
                digit = n % 10
                happySum += digit * digit
                n = n // 10
            
            if happySum in checked:
                return False
            else: 
                checked.append(happySum)

        return True

def main():
    sol = Solution()
    print(sol.isHappy(0))

if __name__ == "__main__":
    main()