class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        counter = {}
        maxF = 0
        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1
            maxF = max(maxF, counter[s[r]])

            while ((r - l + 1) - maxF > k):
                counter[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest