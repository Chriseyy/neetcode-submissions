class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        
        for i in strs:
            len_str = len(i)
            encode_str += f"{len_str}#{i}"
        return encode_str


    def decode(self, s: str) -> List[str]:
        decord_str = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1

            lenght = int(s[i:j])
            start_word = j+1
            end_word = start_word+lenght
            decord_str.append(s[start_word:end_word])
            i = end_word
        return decord_str

