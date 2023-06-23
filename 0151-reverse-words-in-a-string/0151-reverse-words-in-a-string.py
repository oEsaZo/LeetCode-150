class Solution:
    def reverseWords(self, s: str) -> str:
        w = s.split()
        return " ".join(reversed(w))