class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def longestSubstring(s,i):
            d={}
            c=0
            for j in range(i,len(s)):
                if s[j] not in d:
                    d[s[j]]=1
                    c+=1
                else:
                    return c
            # print(d)
            return c
                
        maxi=0
        for i in range(len(s)):
            maxi=max(maxi,longestSubstring(s,i))
        return maxi
        