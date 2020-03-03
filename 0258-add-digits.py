class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            sum = 0

            while num > 9:
                sum += (num % 10)
                num = num // 10
        
            num += sum

        return num

def main():
    sol = Solution()

    print(sol.addDigits(123))

if __name__ == "__main__":
    main()