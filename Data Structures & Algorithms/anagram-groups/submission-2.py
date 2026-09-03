from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_dict = defaultdict(list)
        for string in strs:
            key = "".join(sorted(string))
            output_dict[key].append(string)
        return list(output_dict.values())