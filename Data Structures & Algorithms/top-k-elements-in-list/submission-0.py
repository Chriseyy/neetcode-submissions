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