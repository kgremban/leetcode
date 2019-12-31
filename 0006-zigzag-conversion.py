class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag = [""]
        count = 0
        countUp = True

        for ch in s:
            if not zigzag[count]:
                zigzag.append("")
            
            zigzag[count] = zigzag[count] + ch

            if countUp:
                count += 1
            else:
                count -= 1

            if count == 0:
                countUp = True
            if count == numRows -1:
                countUp = False

        return "".join(zigzag)

def main():
    sol = Solution()

    print(sol.convert("PAYPALISHIRING", 4))

if __name__ == "__main__":
    main()
