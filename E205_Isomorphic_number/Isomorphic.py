class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        res = {}
        
        for i in range(len(s)):

            if s[i] in res:
                if t[i] == res.get(s[i]):
                    continue
                else:
                    return False
            else:
                res[s[i]] = t[i]
        
        res = {}
        
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
    s = "foo"
    t = "bar"
    print(s1.isIsomorphic(s, t))