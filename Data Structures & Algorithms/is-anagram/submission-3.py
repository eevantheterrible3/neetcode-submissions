class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = dict()
        if len(s) != len(t):
            return False
            
        for c in s:
            if c not in map:
                map[c] = 1
            else:
                map[c] += 1
        
        print(map)

        for c in t:
            if (c not in map) or (map[c] == 0):
                return False
            
            map[c] -= 1
        
        print(map)
        return True
        