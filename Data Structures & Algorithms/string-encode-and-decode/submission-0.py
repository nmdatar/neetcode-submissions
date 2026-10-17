class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ''
        for s in strs:
            l = len(s)
            r += str(l) + "#" + s
        return r

    def decode(self, s: str) -> List[str]:
        res = []
        
        i = 0
        curr = 0
        while i < len(s):
            if s[i] != '#':
                curr = curr * 10 + int(s[i])
                i += 1

            else:
                i += 1
                res.append(''.join(s[i:i+curr]))
                i += curr
                curr = 0

        return res            

                