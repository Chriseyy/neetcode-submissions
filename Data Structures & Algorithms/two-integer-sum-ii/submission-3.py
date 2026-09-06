class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_p = 0
        r_p = len(numbers)-1
        while l_p != r_p:
            if numbers[l_p] + numbers[r_p] == target:
                return [l_p+1, r_p+1]
            if numbers[l_p] + numbers[r_p] > target:
                r_p -= 1
            else:
                l_p += 1