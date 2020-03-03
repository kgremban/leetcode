class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        else:
            return sorted(s) == sorted(t)

def main():
    sol = Solution()

    s1 = "anagram"
    t1 = "nagaram"

    s2 = "rat"
    t2 = "car"

    print(sol.isAnagram("hi", ""))

if __name__ == "__main__":
    main()