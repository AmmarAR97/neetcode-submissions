class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        for i, num in enumerate(nums):
            val = target - num
            if val in hash_map:
                return [hash_map[val], i]
            hash_map[num] = i
        return []