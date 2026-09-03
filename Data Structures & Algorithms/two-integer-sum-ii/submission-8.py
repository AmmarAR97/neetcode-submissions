class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_index, right_index = 0, len(numbers) - 1
        while left_index < right_index:
            res = numbers[left_index] + numbers[right_index]
            if res == target:
                print("x")
                return [left_index+1, right_index+1]
            elif res > target:
                right_index -= 1
            else:
                left_index += 1
        return []