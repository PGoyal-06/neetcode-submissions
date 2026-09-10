class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = {}

        for str_ in strs:
            sorted_str = "".join(sorted(str_))
            if sorted_str in group_dict:
                 group_dict[sorted_str].append(str_)
            else:
                 group_dict[sorted_str] = [str_]
        
        return list(group_dict.values())