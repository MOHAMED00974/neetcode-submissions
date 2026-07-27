class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        vis= {}
        l, r= 0, 0
        ans= 0
        CurMax= 0

        while r< len(s):
            vis[s[r]]= vis.get(s[r], 0)+1
            CurMax= max(CurMax, vis[s[r]])

            if (r-l+1) -CurMax<= k:
                r+= 1
                continue
            ans= max(ans, r-l)
            
            while (r-l+1) -CurMax> k:
                vis[s[l]]-= 1
                l+= 1
                CurMax= max(vis.values())
            r+= 1
        ans= max(ans, r-l)
        return ans