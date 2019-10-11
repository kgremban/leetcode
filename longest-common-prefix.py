from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs: 
            return ""

        longestCommonPrefix = strs[0]

        for item in strs:
            commonPrefix = ""
            i = 0

            while (i < len(item)) and (i < len(longestCommonPrefix)) and (item[i] == longestCommonPrefix[i]):
                commonPrefix += item[i]
                i += 1

            if commonPrefix == "": 
                return commonPrefix

            if len(commonPrefix) < len(longestCommonPrefix):
                longestCommonPrefix = commonPrefix

        return longestCommonPrefix

def main(): 
    sol = Solution()

    input1 = ["flower", "flow", "flight"]
    input2 = ["dog", "racecar", "car"]
    input3 = ["aca", "cba"]

    print (sol.longestCommonPrefix(input1))

if __name__ == "__main__":
    main()