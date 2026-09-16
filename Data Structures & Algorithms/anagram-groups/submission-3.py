class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()
        for word in strs:
            sorted_chars = "".join(sorted(word))
            if sorted_chars in res:
                res[sorted_chars].append(word)
            else:
                res[sorted_chars] = [word]
        return list(res.values())