class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lis_s = self.auxCounter(s)
        lis_t = self.auxCounter(t)
        return lis_s == lis_t
    def auxCounter(self, palavra:str):
        dicionario = {}
        for letra in palavra:
            if letra in dicionario:
                dicionario[letra] += 1
            else:
                dicionario[letra] = 1

        return dicionario