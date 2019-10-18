class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: 
            return 0
        
        elif needle in haystack:
            index = 0
            nLength = len(needle)

            while (index + nLength) <= hLength:
                if haystack[ index : (index + nLength) ] == needle:
                    return index
                else:
                    index += 1

        else:
            return -1

def main():
    sol = Solution()

    haystack1 = "hello"
    needle1 = "ll"

    haystack2 = "aaaaa"
    needle2 = "bba"

    haystack3 = "abcde"
    needle3 = "de"

    haystack4 = "aaa"
    needle4 = "a"

    print(sol.strStr(haystack3, needle3))

if __name__ == "__main__":
    main()