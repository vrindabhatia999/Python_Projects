#longest coommon prefix solution:
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ("")

        if len(strs) == 1:
            return (strs[0])

        pref = strs[0]

        plen = len(pref)

        for s in strs[1:]:
            while pref != s[0:plen]:
                pref = pref[0:(plen - 1)]
                plen -= 1

                if plen == 0:
                    return ("")

        return  pref
