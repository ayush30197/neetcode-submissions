class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_string = "#".join(strs)
        return enc_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = s.split("#")
        return decoded_strs
