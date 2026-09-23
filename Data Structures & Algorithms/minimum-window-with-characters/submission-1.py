class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        
        haveMap, needMap = {}, {}
        for c in t:
            needMap[c] = 1 + needMap.get(c, 0)
        
        have, need = 0, len(needMap)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            haveMap[s[r]] = 1 + haveMap.get(s[r], 0)

            if s[r] in needMap and haveMap[s[r]] == needMap[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                haveMap[s[l]] -= 1
                if s[l] in needMap and haveMap[s[l]] < needMap[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""

