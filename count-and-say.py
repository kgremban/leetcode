1
11
21
1211
111221
312211
13112221
1113213211
31131211131221
13211311123113112211
11131221133112132113212221

class Solution:
    def countAndSay(self, n: int) -> str:
        
        count = 1
        base = "1"

        while count < n:
            
            base = self.nextString(base)
            count += 1
        
        return base

    def nextString(self, s: str) -> str:
        next = ""
        index = 0
        count = 0

        while index < len(s):

            if index == len(s) - 1:
                count += 1
                next = next + str(count) + s[index]
                index += 1

            elif s[index] == s[index + 1]:
                count += 1
                index += 1
            
            else:
                count += 1
                next = next + str(count) + s[index]
                count = 0
                index += 1

        return next



def main():
    sol = Solution()

    input1 = 1
    input2 = 4
    input3 = 10

    print(sol.countAndSay(input3))

if __name__ == "__main__":
    main()