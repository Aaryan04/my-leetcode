class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # common = ""
        # strs = sorted(strs)
        # first = strs[0]
        # last = strs[-1]
        # for i in range(min(len(first), len(last))):
        #     if first[i] != last[i]:
        #         return common
        #     common += first[i]
        # return common
        # TC - O(m.nlogn)

        # BETTER APPROACH
        pref = strs[0]
        pref_len = len(pref)

        for s in strs[1:]:
            while pref != s[0:pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ""
                pref = pref[0:pref_len]
        return pref