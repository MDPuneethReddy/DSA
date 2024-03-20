class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        values=[]
        start=intervals[0][0]
        end=intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]>=start and intervals[i][0]<=end:
                if intervals[i][1]>end:
                    end=intervals[i][1]
            else:
                values.append([start,end])
                start=intervals[i][0]
                end=intervals[i][1]
        values.append([start,end])
        return values

        