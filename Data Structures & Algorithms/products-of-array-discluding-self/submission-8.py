class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_num = len(nums)
        
        pref = [0] * len_num
        pref[0] = 1
        for i in range(1, len_num):
            pref[i] = pref[i - 1] * nums[i - 1]

        suff = [0] * len_num
        suff[-1] = 1
        for i in range(len_num-2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]
        
        res = [0] * len_num
        for i in range(len_num):
            res[i] = pref[i] * suff[i]

        return res