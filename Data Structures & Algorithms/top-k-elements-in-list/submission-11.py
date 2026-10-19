class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = dict()
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        return [k for k, _ in sorted(hash_map.items(), key=lambda item: item[1], reverse=True)[:k]]