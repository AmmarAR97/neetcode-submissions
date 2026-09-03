# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         left_index, right_index = 0, len(numbers) - 1
#         while left_index < right_index:
#             res = numbers[left_index] + numbers[right_index]
#             if res == target:
#                 print("x")
#                 return [numbers[left_index], numbers[right_index]]
#             elif res > target:
#                 right_index -= 1
#             else:
#                 left_index -= 1
            
            
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []