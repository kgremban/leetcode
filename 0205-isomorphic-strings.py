class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        isIso = True

        sSeen = [] 
        tSeen = []

        # Scan through both strings in parallel
        for sChar, tChar in zip(s, t):

            # If we've seen these characters before, check that we first
            # saw them at the same index. Otherwise, not isomorphic
            if sChar in sSeen and tChar in tSeen:
                if sSeen.index(sChar) == tSeen.index(tChar):
                    continue
                else: 
                    isIso = False

            # If we've seen one character but not the other, 
            # not isomorphic
            elif sChar in sSeen or tChar in tSeen:
                isIso = False

            # If they're both new characters, append them to the seen lists
            else:
                sSeen.append(sChar)
                tSeen.append(tChar)

        return isIso

    def isIsomorphicFaster(self, s: str, t: str) -> bool:

        # Zipping the strings makes a list of tuples so that the first element
        # in s is paired with the first element in t, then the second elements,
        # third, etc. Getting the set of the zipped strings eliminates duplicates.
        # The length of the sip set should be the length of the s set and the 
        # length of the t set if they all share the same pattern. 
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

def main():
    sol = Solution()

    s1 = "egg"
    t1 = "add"

    s2 = "foo"
    t2 = "bar"

    s3 = "paper"
    t3 = "title"

    s4 = "a"
    t4 = "b"

    print(sol.isIsomorphic(s3, t3))
    print(sol.isIsomorphicFaster(s3, t3))

if __name__ == "__main__":
    main()