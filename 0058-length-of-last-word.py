class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()

        if words:
            return len(words[-1])        
        else: 
            return 0

def main():
    sol = Solution()

    input1 = "Hello World"
    input2 = "Mississippi"
    input3 = " "

    print(sol.lengthOfLastWord(input3))

if __name__ == "__main__":
    main()