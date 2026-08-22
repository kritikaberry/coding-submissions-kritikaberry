class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      #vertical scanning
      if not strs:
        return ""
        
      first = strs[0]
      for i in range(len(first)):
        for s in strs:
            if i == len(s) or s[i]!=first[i]:
                return first[:i]
      return first #if same for all strings in str then return back the first