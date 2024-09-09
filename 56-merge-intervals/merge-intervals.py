class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:(x[0]))
        mainValue=[intervals[0]]
        mainList=[]
        for i in range(1,len(intervals)):
            if mainValue[0][1]>=intervals[i][0]:
                mainValue[0]=[mainValue[0][0],max(mainValue[0][1],intervals[i][1])]
            else:
                mainList.append(mainValue.pop())
                mainValue.append(intervals[i])
        if len(mainValue)>0:
            mainList.append(mainValue[0])
        return mainList
        