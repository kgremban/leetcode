class Solution:
    def isValid(self, s: str) -> bool:
        # Check if string has equal numbers of open and closed parentheses
        if (s.count('(') != s.count(')')) or (s.count('[') != s.count(']')) or (s.count('{') != s.count('}')):
            return False

        stack = []
        for char in s: 
            # Put open parentheses in a stack
            if char in ['(', '[', '{']:
                stack.append(char)

            # For every closed parenthesis, the last item on the stack should be its match
            # Also catch any unapproved characters
            else:
                pair = stack.pop() + char
                if pair not in ['()', '[]', '{}']:
                    return False

        # Accept empty strings
        return True

def main():
    #input = "()"
    input = "()[]d{}"
    #input = "(]"
    #input = "([)]"
    #input = "{[]}"
    #input = ""

    sol = Solution()
    print(sol.isValid(input))

if __name__ == "__main__":
    main()