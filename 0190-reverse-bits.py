class Solution:
    def reverseBits(self, n: int) -> int:
        
        binary = bin(n)
        reverse = binary[-1:1:-1]
        reverse = reverse + (32 - len(reverse))*'0'

        return int(reverse, 2)

    def reverseBitsBitwise(self, n: int) -> int:
        rev = 0
        for i in range(32):
            # d is the last digit from n
            d = n & 1

            # shift to remove d
            n >>= 1

            # move rev to add a space and add d at the units place
            rev <<= 1
            rev = rev | d

        return rev


def main():
    sol = Solution()

    input1 = 43261596
    input2 = 4294967293

    print(sol.reverseBitsBitwise(input2))

if __name__ == "__main__":
    main()