class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) > 0:
            return "abra-ca-dabra".join(strs)
        return "None"

    def decode(self, s: str) -> List[str]:
        if s != "None":
            return s.split("abra-ca-dabra")
        return []
