from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if not nums: 
            return 0
        
        index = 0
        compare = nums[0]

        for num in nums: 
            if num > compare: 
                index += 1
                nums[index] = num
                compare = nums[index]
        
        return index + 1

def main():
    sol = Solution()

    list1 = [1,1,2]
    list2 = [0,0,1,1,1,2,2,3,3,4]
    list3 = [1]
    list4 = []
    list5 = [0,0,0,0,0,0,0,0,2]

    print(sol.removeDuplicates(list2))
    print(list2)

if __name__ == "__main__":
    main()