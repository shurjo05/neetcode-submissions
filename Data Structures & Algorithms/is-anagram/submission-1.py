class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        schs = sorted(list(s))
        tchs = sorted(list(t))
        if (schs == tchs) :
            return True
        return False