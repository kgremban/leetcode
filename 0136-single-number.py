from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        singletons = []

        for num in nums:
            if num not in singletons:
                singletons.append(num)
            else:
                singletons.remove(num)

        return singletons[0]

    def singleNumber_hash(self, nums: List[int]) -> int:
        isSingle = {}

        for num in nums:
            try:
                isSingle.pop(num)
            except:
                isSingle[num] = True
        

        return isSingle.popitem()[0]

    def singleNumber_math(self, nums: List[int]) -> int:
        return (2 * sum(set(nums))) - sum(nums)

def main():
    sol = Solution()

    input1 = [2, 2, 1]
    input2 = [4, 1, 2, 1, 2]

    print(sol.singleNumber(input2))

if __name__ == "__main__":
    main()