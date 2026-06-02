class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        all_values = {}
        for i in range(len(nums)):
            if nums[i] in all_values:
                return True
            else:
                all_values.update({nums[i]: nums[i]})
        return False

        