class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s, letters_t = {}, {}
        for i in range(len(s)):
            letters_s.update({s[i]: (letters_s.get(s[i]) or 0)+1})
        for j in range(len(t)):
            letters_t.update({t[j]: (letters_t.get(t[j]) or 0)+1})
        return letters_s == letters_t