class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]
        for st in strs:
            while not st.startswith(pre):
                pre = pre[:-1]
        return pre

        