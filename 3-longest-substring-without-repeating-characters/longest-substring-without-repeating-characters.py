class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        unique=set()
        unique.add(s[0])
        # values=[s[0]]
        i=0
        j=1
        count=1
        maxi=0
        while(i<=j and j<len(s) and i<len(s)):
            if s[j] in unique:
                maxi=max(maxi,count)
                while(1):
                    unique.remove(s[i])
                    if s[j] in unique:
                        i+=1
                    else:
                        unique.add(s[j])
                        i+=1
                        count=j-i+1
                        j+=1
                        break 
            else:
                count+=1
                unique.add(s[j])
                # values.append(s[j])
                j+=1
        maxi=max(maxi,count)
        return maxi
