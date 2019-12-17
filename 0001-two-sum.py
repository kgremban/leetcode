class Solution:
    def twoSum(self, nums, target):
        enums = list(enumerate(nums))
        for idx, i in enums:
            if i > target:
                continue
            #print("i = ", i)
            for jdx, j in enums:
                if j > target:
                    continue
                #print("j = ", j)
                if (idx != jdx and i + j == target):
                    return [idx, jdx]
        

def main():
    ints1 = [1,20,7,11,15]
    target1 = 18
    ints2 = [3,2,4]
    target2 = 6
    ints3 = [3,3]
    target3 = 6
    sol = Solution()
    print(sol.twoSum(ints4, target4))

if __name__ == "__main__":
    main()