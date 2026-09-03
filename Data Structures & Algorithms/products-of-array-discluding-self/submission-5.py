class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # method 1:
        # len_nums = len(nums)
        # res = [0] * len_nums
        # for i in range(len_nums):
        #     prod = 1
        #     for j in range(len_nums):
        #         if i == j:
        #             continue
        #         prod *= nums[j]
        #     res[i] = prod
        # return res

        # method 2:
        # len_nums = len(nums)
        
        # pref = [0] * len_nums
        # pref[0] = 1
        # for i in range(1, len_nums):
        #     pref[i] = nums[i - 1] * pref[i - 1]
        
        # suff = [0] * len_nums
        # suff[len_nums-1] = 1
        # for i in range(len_nums-2, -1, -1):
        #     suff[i] = nums[i + 1] * suff[i + 1]
        
        # res = [0] * len_nums
        # for i in range(len_nums):
        #     res[i] = pref[i] * suff[i]
        
        # return res
        
        # method 3:
        len_nums = len(nums)
        zero_count = 0
        prod = 1
        res = [0] * len_nums

        for num in nums:
            if num:
                prod *= num
            else:
                zero_count += 1

        if zero_count > 1:
            return res
        
        for i in range(len_nums):
            if zero_count:
                if nums[i] == 0:
                    res[i] = prod
            else:
                res[i] = prod // nums[i]
        
        return res


