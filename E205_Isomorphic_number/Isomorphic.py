class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        res = {}
        
        for i in range(len(s)):

            # Check if char is in dict
            if s[i] in res:
                if t[i] == res.get(s[i]): # Check if associated position in t map to same char
                    continue
                else:
                    return False
            else:
                res[s[i]] = t[i] # add new char to the dict
        
        res = {}
        
        # Repeat again to prevent badc and baba (no two characters can map to the same char)
        for i in range(len(t)):

            if t[i] in res:
                if s[i] == res.get(t[i]):
                    continue
                else:
                    return False
            else:
                res[t[i]] = s[i]

        return True

if __name__ == "__main__":

    s1 = Solution()

    # True
    s = "paper"
    t = "title"
    print(s1.isIsomorphic(s, t))

    # False
    s = "badc"
    t = "baba"
    print(s1.isIsomorphic(s, t))