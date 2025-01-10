class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window 2 pointer time complexity-o(n), space complexity- o(n)
        d={}
        left=0
        right=0
        output=0
        while(right<len(s)):
            # print(d)
            if s[right] in d:
                left=max(left,d[s[right]]+1)
            d[s[right]]=right
            output=max(output,right-left+1)
            # print(output)
            right+=1
        return output

        