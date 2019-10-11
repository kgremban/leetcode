from fractions import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check that the shorter string exists within the longer string
        if (str1 not in str2) and (str2 not in str1):
            return ""

        # Find the GCD of both strings, which is the max pattern length
        maxLength = gcd(len(str1), len(str2))

        # Find the basic pattern in each string
        pattern1 = findDivisor(str1, maxLength)
        pattern2 = findDivisor(str2, maxLength)

        # Make sure the basic patterns match
        if pattern1 != pattern2:
            return ""

        # Divide the lengths of both strings by the length of the pattern, then calculate GCD
        # The result is the number of times the pattern can repeat
        patternCount = gcd((len(str1)/len(pattern1)), (len(str2)/len(pattern1)))
        greatestCommonString = pattern1 * int(patternCount)
        return greatestCommonString

def findDivisor(s: str, l: float) -> str:
        count = 0
        # Start building the pattern with the first character of s
        sPattern = s[0]
        # Create a test case by moving the first character of s to the end
        sTest = s[1:] + s[0]

        while (sTest != s) and (count < l):
            sPattern += sTest[0]
            sTest = sTest[1:] + sTest[0]
            count += 1

        return sPattern

def main():
    str1 = "ABCABCABCABCABCABCABCABCD"
    str2 = "ABCABCABCABC"
    
    #str1 = "ABABAB"
    #str2 = "ABAB"

    #str1 = "LEET"
    #str2 = "CODE"

    sol = Solution()

    print(sol.gcdOfStrings(str1, str2))

if __name__ == "__main__":
    main()