class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)

        prefix = [0] * nums_length
        prefix[0] = 1
        for i in range(1, nums_length):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        suffix = [0] * nums_length
        suffix[-1] = 1
        for i in range(nums_length-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        res = [0] * nums_length
        for i in range(nums_length):
            res[i] = prefix[i] * suffix[i]
        
        return res