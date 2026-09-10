class Solution:


    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        delimiter = ","
        for str_ in strs:
            length = len(str_)
            encoded_string += str(length) + delimiter + str_
        return encoded_string

    def decode(self, s: str) -> List[str]:
        pointer = 0
        delimiter = ","
        result = []
        while pointer < len(s):
            delim_pos = s.find(delimiter, pointer)
            length = int(s[pointer: delim_pos])
            pointer = delim_pos + 1 + length
            result.append(s[delim_pos + 1: pointer]) 
        return result
