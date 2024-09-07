class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        mainList=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                mainList.append("FizzBuzz")
            elif i%3==0 and i%5!=0:
                mainList.append("Fizz")
            elif i%3!=0 and i%5==0:
                mainList.append("Buzz")
            else:
                mainList.append(str(i))
        return mainList
        