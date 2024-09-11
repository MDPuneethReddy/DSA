class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d={}
        for i in text:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        c=len(text)
        # print(c)
        chars=["b","a","l","o","n"]
        for i in chars:
            if i not in d:
                # print("yes")
                return 0
            else:
                # print(d[i],i)
                if i in ["l","o"]:
                    c=min(c,d[i]//2)
                    print(c)
                else:
                    c=min(c,d[i])
                    print(c)
        return c

        