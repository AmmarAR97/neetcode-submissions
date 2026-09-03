class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_dict = {}

        for string in strs:
            sorted_string = "".join(sorted(string))
            if output_dict.get(sorted_string):
                output_dict[sorted_string].append(string)
            else:
                output_dict[sorted_string] = [string]
        
        return [v for v in output_dict.values()]
        