class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "0rsha"
        else:
            return "#Arsha#".join(strs)
    def decode(self, s: str) -> List[str]:
        if s is "0rsha":
            return []
        else:
            return s.split("#Arsha#")