class Solution: 
    def maxNumberOfBalloons(self, text: str) -> int:
        numA = numB = numL = numO = numN = 0
        for char in text:
            if char not in ['a','b','l','n','o']:
                continue
            if char == 'a':
                numA += 1
                print("Debug")
                continue
            if char == 'b':
                numB += 1
                continue
            if char == 'l': 
                numL += 1
                continue
            if char == 'n':
                numN += 1
                continue
            if char == 'o':
                numO += 1
                continue

        numL = numL // 2
        numO = numO // 2
       
        return min(numA, numB, numL, numO, numN)

def main():
    sol = Solution()
    text1 = "nlaebolko"
    text2 = "loonbalxballpoon"
    text3 = "leetcode"
    text4 = "balon"

    print(1 // 2)
    print(sol.maxNumberOfBalloons(text4))

if __name__ == "__main__":
    main()
