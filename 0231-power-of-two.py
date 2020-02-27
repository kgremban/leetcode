class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
            
        return (n & n-1) == 0

def main():
    sol = Solution()

    print(sol.isPowerOfTwo(0))

if __name__ == "__main__":
    main()