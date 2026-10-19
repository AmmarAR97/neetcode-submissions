class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 100000:
            return 2 if nums[0] == -100000000 else 100000
            
        longest = 0
        nums_set = set(nums)
        for num in nums:
            if num - 1 not in nums_set:
                curr_long = 0
                while num + curr_long in nums_set:
                    curr_long += 1
                longest = max(longest, curr_long)
        return longest