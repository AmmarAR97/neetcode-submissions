class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            op = 1
            for j in range(len(nums)):
                if i != j:
                    op *= nums[j]
            res.append(op)
        return res