class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapa, mapb = {}, {}
        for i in list(s):
            if i in mapa.keys():
                mapa[i] += 1
            else:
                mapa[i] = 1
        

        for i in list(t):
            if i in mapb.keys():
                mapb[i] += 1
            else:
                mapb[i] = 1

        return True if mapa == mapb else False