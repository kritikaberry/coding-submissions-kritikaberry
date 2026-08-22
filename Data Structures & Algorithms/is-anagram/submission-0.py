class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t) == 0):
            return False
        count = 0
        checkDictS = {}
        checkDictT = {}
        for i in range(len(s)):
            if(s[i] not in checkDictS.keys()):
                checkDictS[s[i]] = 1
            else:
                checkDictS[s[i]] += 1
        for j in range(len(t)):
            if(t[j] not in checkDictT.keys()):
                checkDictT[t[j]] = 1
            else:
                checkDictT[t[j]] += 1
        if checkDictS == checkDictT:
            return True
        return False