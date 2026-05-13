class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l=sorted(t)
        m=sorted(s)
        if l==m:
            return True 
        return False