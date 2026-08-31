class Solution:
    def minWindow(self, s: str, t: str) -> str:
        wantedChars= {}
        for x in t:
            wantedChars[x]= wantedChars.get(x, 0)+1
        
        unique= len(wantedChars)
        l, r= 0, 0
        cur= ""

        while r< len(s):
            if wantedChars.get(s[r], None) != None:

                wantedChars[s[r]]-= 1

                if wantedChars[s[r]]== 0:
                    unique-= 1
            r+= 1

            if unique:
                continue
            
            while l< r and not unique:
                if s[l] not in wantedChars:
                    l+= 1
                else:
                    wantedChars[s[l]]+= 1
                    if wantedChars[s[l]]> 0:
                        unique+= 1
                    else:
                        l+= 1
                    
            
            if cur== "" or len(cur)> r-l:
                cur= s[l:r]
            l+= 1

        return cur