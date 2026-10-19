class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs:
            encoded_string = "-#$%-".join(strs)
        else:
            encoded_string = "-#$%*-"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if s == "-#$%*-":
            decoded_strs = []
        else:
            decoded_strs = s.split("-#$%-")
        return decoded_strs
