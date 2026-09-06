class Solution:
  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    groups = {}
    for s in strs:
      sorted_key = "".join(sorted(s))
      if sorted_key not in groups:
        groups[sorted_key] = []
      groups[sorted_key].append(s)
    return list(groups.values())


## whitout sort:
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

#         result = defaultdict(list) # charCount : list of anagrams

#         for word in strs:
#             charCount = [0] * 26 # a ... z

#             for char in word:
#                 charCount[ord(char) - ord("a")] += 1

#             result[tuple(charCount)].append(word)

#         return list(result.values())