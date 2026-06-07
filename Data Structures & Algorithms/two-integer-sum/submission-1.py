class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i, num in enumerate(nums):
            if numbers.get(target-num) != None:
                return [numbers.get(target-num), i]
            else:
                numbers.update({num: i})
        return list()
            
            