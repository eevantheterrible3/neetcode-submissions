class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        array = [[] for i in range(len(nums) + 1)]

        for n, c in freq.items():
            array[c].append(n)

        res = []

        for i in range(len(array) - 1, 0, -1):
            for e in array[i]:
                res.append(e)
                if len(res) == k:
                    return res