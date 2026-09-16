class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs:
            return "#@$".join(strs)
        return "PAPAPA"

    def decode(self, s: str) -> List[str]:
        if s == "PAPAPA":
            return []
        if s == "":
            return [""]
        return s.split("#@$")