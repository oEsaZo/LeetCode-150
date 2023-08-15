class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n, result, seen, left = len(s), 0, {}, 0
        if n <= 1:
            return n
        for right, char in enumerate(s):
            if char in seen:
                left = max(left, seen[char]+1)
            result = max(result, right - left +1)
            seen[char] = right
        return result                            