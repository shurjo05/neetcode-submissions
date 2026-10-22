class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        count = 0
        for n in hs:
            if n - 1 not in hs:
                longest = 1
                while n + 1 in hs:
                    longest += 1
                    n += 1
                if longest > count:
                    count = longest
        return count