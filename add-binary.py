class Solution:
    def addBinary(self, a: str, b: str) -> str:
        binarySum = ""
        carry1 = False

        # Fill in 0's on the shorter number to make both strings equal lengths
        maxBinary = max(a, b, key=len)
        minBinary = a.rjust(len(maxBinary), "0") if a != maxBinary else b.rjust(len(maxBinary), "0")

        # Scan both strings right to left and add bits. Carry the 1 with boolean flag
        for i, j in zip(maxBinary[::-1], minBinary[::-1]):
            if i == "1" and j == "1":
                if carry1:
                    binarySum = "1" + binarySum
                else:
                    binarySum = "0" + binarySum
                    carry1 = True

            if i != j:
                if carry1:
                    binarySum = "0" + binarySum
                else: 
                    binarySum = "1" + binarySum

            if i == "0" and j == "0":
                if carry1:
                    binarySum = "1" + binarySum
                    carry1 = False
                else: 
                    binarySum = "0" + binarySum

        # Add new digit if we got to the end of both strings and need to carry the 1
        if carry1:
            binarySum = "1" + binarySum

        return binarySum

    def addBinaryNum(self, a: str, b: str) -> str: 
        
        # Convert strings to base-2 integers
        binA = int(a, 2)
        binB = int(b, 2)

        # Add and return in string format
        return format((binA + binB), 'b')

def main():
    sol = Solution()

    a1 = "11"
    b1 = "1"

    a2 = "1010"
    b2 = "1011"

    a3 = "11111"
    b3 = "10000001"

    print(sol.addBinaryNum(a3, b3))

if __name__ == "__main__":
    main()