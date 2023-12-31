class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s1=""
        for i in s:
            if i.isalnum():
                s1+=i
        print(s1)
        for i in range(len(s1)//2):
            if s1[i]!=s1[len(s1)-i-1]:
                return False
        return True
        