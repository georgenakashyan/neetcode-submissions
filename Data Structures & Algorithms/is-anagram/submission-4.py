class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = {}
        for i in range(len(s)):
            letters.update({s[i]: (letters.get(s[i]) or 0)+1})
            if (letters.get(s[i]) == 0):
                letters.pop(s[i])
            letters.update({t[i]: (letters.get(t[i]) or 0)-1})
            if (letters.get(t[i]) == 0):
                letters.pop(t[i])
        return len(letters) == 0