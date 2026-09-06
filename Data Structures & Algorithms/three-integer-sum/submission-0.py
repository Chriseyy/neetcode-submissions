class Solution:

  def threeSum(self, nums: list[int], target: int = 0) -> list[list[int]]:
    found = []
    nums.sort()
    n = len(nums)

    for i in range(n - 2):
      if nums[i] > 0:
        break
        
      if i > 0 and nums[i] == nums[i - 1]:
        continue

      l_p = i + 1
      r_p = n - 1

      while l_p < r_p:
        total = nums[i] + nums[l_p] + nums[r_p]

        if total > 0:
          r_p -= 1
        elif total < 0:
          l_p += 1
        else:
          found.append([nums[i], nums[l_p], nums[r_p]])
          l_p += 1
          r_p -= 1

          while l_p < r_p and nums[l_p] == nums[l_p - 1]:
            l_p += 1

    return found