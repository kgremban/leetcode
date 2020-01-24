class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        maxSubstring = s[0]
        maxLength = 1

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    string = s[i:j+1]
                    revString = string[::-1]

                    if string == revString and (j+1 - i) > maxLength:
                        maxSubstring = string
                        maxLength = len(maxSubstring)
        
        return maxSubstring

def main():
    sol = Solution()

    input1 = "babad"
    input2 = "cbbd"
    input3 = "a"

    print(sol.longestPalindrome(input3))

if __name__ == "__main__":
    main()