class Solution:
  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    groups = {}
    for s in strs:
      sorted_key = "".join(sorted(s))
      if sorted_key not in groups:
        groups[sorted_key] = []
      groups[sorted_key].append(s)
    return list(groups.values())