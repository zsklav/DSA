class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        n=len(intervals)
        prev=intervals[0]
        if n==1:
            return n
        count=0
        i=1
        while i<n:
            a=prev[0]
            b=prev[1]
            c=intervals[i][0]
            d=intervals[i][1]
            if c>=a and d<=b:
                count+=1
            else:
                prev=intervals[i]
            i+=1
        return n-count

        