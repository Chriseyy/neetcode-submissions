class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rest_num = dict()

        for i in range(len(nums)):
            left = target - nums[i]
            if left in rest_num:
                return [rest_num[left],i]
            rest_num[nums[i]] = i
        return []