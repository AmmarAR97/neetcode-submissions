class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        
        pref = [0] * len_nums
        pref[0] = 1
        for i in range(1, len_nums):
            pref[i] = pref[i-1] * nums[i-1]
        
        suff = [0] * len_nums
        suff[-1] = 1
        for i in range(len_nums-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]

        res = [0] * len_nums
        for i in range(len_nums):
            res[i] = pref[i] * suff[i]
        
        return res