class Solution:
    def isPeak(self, itms):
        flag = itms[1]> itms[0] and itms[1] >= itms[2]
        flag = flag or (itms[1]>= itms[0] and itms[1]> itms[2])
        return flag

    def maxTwoPeaks(self, l, r, peaks, highs):
        MaxR= r
        while r< len(peaks) and highs[peaks[MaxR]]< highs[peaks[l]]:
            MaxR= r if highs[peaks[MaxR]]< highs[peaks[r]] else MaxR
            r+= 1
        
        return l, MaxR
            
    def trap(self, height: List[int]) -> int:
        n= len(height)
        peaks= []

        try:
            if height[0]>height[1]:
                peaks.append(0)
        except:
            return 0

        for x in range(1, n-1):
            if self.isPeak(height[x-1:x+2]):
                peaks.append(x)
        
        if height[n-1]> height[n-2]:
            peaks.append(n-1)
        
        l, r= 0, 1
        ans= 0
        while r< len(peaks):
            l, r= self.maxTwoPeaks(l, r, peaks, height)
            minimum= min(height[peaks[l]], height[peaks[r]])
            
            for x in range(peaks[l], peaks[r]):
                ans+= max(minimum- height[x], 0)
            l= r
            r= l+1
        
        return ans
