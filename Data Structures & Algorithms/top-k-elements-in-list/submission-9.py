class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = dict()
        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        return [key for key, _ in sorted(seen.items(), key=lambda item: item[1], reverse=True)[:k]]