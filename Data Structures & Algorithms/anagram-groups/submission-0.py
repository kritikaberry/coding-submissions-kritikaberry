class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]
        
        sortDict = defaultdict(list)
        for word in strs:
            sWord = "".join(sorted(word))
            sortDict[sWord].append(word)
        
        return list(sortDict.values())