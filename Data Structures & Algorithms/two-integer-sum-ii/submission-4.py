class Solution:
  def twoSum(self, numbers: list[int], target: int) -> list[int]:
    l_p = 0
    r_p = len(numbers) - 1
    while l_p < r_p:
      cur_sum = numbers[l_p] + numbers[r_p]

      if cur_sum == target:
        return [l_p + 1, r_p + 1]
      elif cur_sum > target:
        r_p -= 1
      else:
        l_p += 1

    return []