class Solution:
    def convertToTitle(self, n: int) -> str:
        alph = {
            0: "Z",
            1: "A", 
            2: "B", 
            3: "C", 
            4: "D", 
            5: "E", 
            6: "F", 
            7: "G", 
            8: "H", 
            9: "I", 
            10: "J", 
            11: "K", 
            12: "L", 
            13: "M", 
            14: "N", 
            15: "O",
            16: "P",
            17: "Q", 
            18: "R",
            19: "S",
            20: "T",
            21: "U", 
            22: "V",
            23: "W",
            24: "X",
            25: "Y",
            26: "Z"
        }
        
        title = ""

        while n > 0:
            digit = n % 26
            title = alph.get(digit) + title

            if digit == 0:
                n -= 26
            else: 
                n -= digit 

            n = n // 26

        return title

def main():
    sol = Solution()

    input1 = 1
    input2 = 28
    input3 = 703
    input4 = 14500

    print(sol.convertToTitle(input4))

if __name__ == "__main__":
    main()