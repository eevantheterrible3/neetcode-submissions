class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

        
        

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            digits = []
            j = i

            while s[j] != '#':
                digits.append(s[j])
                j += 1
            
            digits = "".join(digits)
            digits = int(digits)
            print(digits)

            tmp = []
            for c in range(j + 1, j + 1 + digits):
                tmp.append(s[c])
            
            res.append("".join(tmp))
            i = j + digits + 1
        
        return res


        
