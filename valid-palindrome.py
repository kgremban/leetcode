import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''.join(ch for ch in s if ch.isalnum())
        st = st.casefold()

        if st == st[::-1]:
            return True

        return False

def main():
    sol = Solution()

    input1 = "A man, a plan, a canal: Panama"
    input2 = "race a car"

    print(sol.isPalindrome(input2))

if __name__ == "__main__":
    main()