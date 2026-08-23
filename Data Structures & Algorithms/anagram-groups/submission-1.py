class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]
        
        sortDict = defaultdict(list)
        Acount = ord("a")
        for word in strs:
            count = [0] * 26 #to create a character count key
            for c in word:
                count[ord(c) - Acount]+=1
            sortDict[tuple(count)].append(word)
        return list(sortDict.values())