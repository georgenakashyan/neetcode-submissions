class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s = sorted(s)
        t = sorted(t)

        while (len(s) != 0):
            if (s.pop() != t.pop()):
                return False
        return True