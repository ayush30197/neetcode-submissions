class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_string = "ayush".join(strs)
        return enc_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = s.split("ayush")
        return decoded_strs
