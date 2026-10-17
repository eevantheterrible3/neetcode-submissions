class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_char_counter = [0] * 26
        
        for s in s1:
            s1_char_counter[ord(s) - ord("a")] += 1
        
        k = len(s1)

        window_counter = [0] * 26

        for c in range(k):
            window_counter[ord(s2[c]) - ord("a")] += 1
        
        if s1_char_counter == window_counter:
            return True
        
        for r in range(k, len(s2)):
            window_counter[ord(s2[r-k]) - ord("a")] -= 1
            window_counter[ord(s2[r]) - ord("a")] += 1

            if window_counter == s1_char_counter:
                return True
        
        return False
        
            


