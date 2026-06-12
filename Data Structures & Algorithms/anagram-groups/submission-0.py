class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo= {}
        for cur in strs:
            tmp= ''.join(sorted(cur))

            if memo.get(tmp):
                memo[tmp].append(cur)
                continue
            memo[tmp]= []
            memo[tmp].append(cur)
        
        print(list(memo.values()))
        return list(memo.values())
