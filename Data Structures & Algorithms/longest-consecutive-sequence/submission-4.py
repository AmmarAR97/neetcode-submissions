class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)
        for num in nums:
            if num - 1 not in nums_set:
                curr_long = 0
                while num + curr_long in nums_set:
                    curr_long += 1
                longest = max(longest, curr_long)
        return longest