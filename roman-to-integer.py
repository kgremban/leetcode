class Solution:
    def romanToInt(self, s: str) -> int:
        
        romanDict = {
            "I": 1,
            "V": 5, 
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        value = 0
        pVal = 0
        reverseS = s[::-1]

        for char in reverseS: 
            cVal = romanDict[char]
            
            if cVal >= pVal:
                value += cVal

            else:
                value -= cVal

            pVal = cVal

        return value

def main():
    sol = Solution()

    input1 = "III"
    input2 = "IV"
    input3 = "IX"
    input4 = "LVIII"
    input5 = "MCMXCIV"

    print(sol.romanToInt(input5))

if __name__ == "__main__":
    main()