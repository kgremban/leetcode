class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)

        maxSubstring = len(set(s))

        if maxSubstring == 1 or maxSubstring == 2:
            return maxSubstring

        testLength = maxSubstring

        while testLength > 2:

            pointer = 0

            while pointer <= (len(s) - testLength):
                testString = s[pointer : (pointer + testLength)]
                if len(testString) == len(set(testString)):
                    return testLength

                pointer += 1
            testLength -= 1

        return 2

def main(): 
    sol = Solution()

    input1 = "abcabcbb"
    input2 = "bbbbb"
    input3 = "pwwkew"
    input4 = "nfpdmpi"

    print(sol.lengthOfLongestSubstring(input4))

if __name__ == "__main__":
    main()