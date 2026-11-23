class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)

        for num in nums:
            if num not in res:
                res[num] = 1
            else:
                res[num] += 1
        
        sortedRes = list(sorted(res, key=lambda x: res[x], reverse=True))
        return sortedRes[:k]