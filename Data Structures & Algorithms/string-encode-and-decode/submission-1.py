class Solution:

    def encode(self, strs: List[str]) -> str:
        cur= ""
        for x in strs:
            cur= cur+x
            cur= cur+'>>'
        return cur

    def decode(self, s: str) -> List[str]:
        ans= s.split('>>')
        ans.pop()
        return ans