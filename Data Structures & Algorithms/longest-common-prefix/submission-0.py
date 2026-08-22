class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        #sorting method
        prefix = []
        strs.sort() #sorts inplace lexicographically
        first = strs[0]
        last = strs[len(strs)-1]

        for i in range(min(len(first),len(last))):
            if first[i] != last[i]:
                break
            prefix.append(first[i])
        
        return "".join(prefix)