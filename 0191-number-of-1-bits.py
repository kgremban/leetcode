class Solution: 
    def hammingWeight(self, n: int) -> int:
        count = 0

        for i in range(32):
            # retrieve first bit
            b = n & 1

            # move n forward 1 bit
            n >>= 1

            # if b is a 1, count it
            if b: 
                count += 1
        
        return count

def main():
    sol = Solution()

    input1 = int('00000000000000000000000000001011', 2)
    input2 = int('00000000000000010000000000000000', 2)
    input3 = int('11111111111111111111111111111101', 2)

    print(sol.hammingWeight(input3))

if __name__ == "__main__":
    main()