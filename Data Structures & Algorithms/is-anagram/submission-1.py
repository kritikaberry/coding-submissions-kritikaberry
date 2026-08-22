class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False

        counterDict = {}
        for i in s:
            counterDict[i] = counterDict.get(i,0) + 1

        for i in t:
            counterDict[i] = counterDict.get(i,0) - 1

        if all(val == 0 for val in counterDict.values()):
            return True

        return False