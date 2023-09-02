class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)
        if (c1 & c2) == c1:
            return True
        else:
            return False        