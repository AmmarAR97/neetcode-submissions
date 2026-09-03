class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = dict()
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        sorted_dict = dict(sorted(seen.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_dict.keys())[:k]