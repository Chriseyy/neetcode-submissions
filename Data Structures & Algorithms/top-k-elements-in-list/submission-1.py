class Solution:

  def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    topk_dict = {}
    for i in nums:
      if i in topk_dict:
        topk_dict[i] += 1
      else:
        topk_dict[i] = 1

    sorted_items = sorted(
        topk_dict.items(), key=lambda x: x[1], reverse=True
    )

    return [item[0] for item in sorted_items[:k]]




## 

# class Solution:
#   def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#     count = {}
#     freq = [[] for _ in range(len(nums) + 1)]

#     for n in nums:
#       count[n] = 1 + count.get(n, 0)

#     for n, c in count.items():
#       freq[c].append(n)

#     res = []
#     for i in range(len(freq) - 1, 0, -1):
#       for n in freq[i]:
#         res.append(n)
#         if len(res) == k:
#           return res