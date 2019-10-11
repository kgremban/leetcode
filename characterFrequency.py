from typing import List

class Solution: 
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        return self.f(words[0])

    def f(self, s: str) -> int:
        return 0

def main():
    sol = Solution()

    queries1 = ["cbd"]
    words1 = ["zaaaz"]

    queries2 = ["bbb", "cc"]
    words2 = ["a","aa","aaa","aaaa"]

    print(sol.numSmallerByFrequency(queries1, words1))

if __name__ == "__main__":
    main()