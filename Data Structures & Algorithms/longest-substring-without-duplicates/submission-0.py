class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        vis= {}
        l, r= 0, 0
        ans= 0
        
        while r< len(s):
            vis[s[r]]= vis.get(s[r], 0)+1
            if vis[s[r]]<= 1:
                r+= 1
                continue
            ans= max(ans, r-l)
            while vis[s[r]]> 1:
                vis[s[l]]-= 1
                l+= 1
            r+= 1
        ans= max(ans, r-l)
        return ans