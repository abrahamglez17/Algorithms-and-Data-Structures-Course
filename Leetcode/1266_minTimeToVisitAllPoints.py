class Solution:
    def minTimeToVisitAllPoints(self, points):
        dx=0
        dy=0
        tempTuple =[0,0]
        solution= 0
        for point in points:
            if(tempTuple[0]==0 and tempTuple[1]==0):
                tempTuple=point
                continue
            else:
                dx=abs(point[0]-tempTuple[0])
                dy=abs(point[1]-tempTuple[1])
                solution+=max(dx,dy)
                tempTuple=point
        return solution
        
case1= [[1,1],[3,4],[-1,0]]
case2= [[3,2],[-2,2]]
s= Solution()
print(case1)
print(s.minTimeToVisitAllPoints(case1))
print(case2)
print(s.minTimeToVisitAllPoints(case2))

class CleanSolution:
    def minTimeToVisitAllPoints(self, points):
        dx=0
        dy=0
        solution=0
        
        for i in range(1, len(points)):
            dx=abs(points[i][0]-points[i-1][0])
            dy=abs(points[i][1]-points[i-1][1])
            solution+= max(dx,dy)
        return solution

s2= CleanSolution()
print("CLEAN SOLUTION")
print(case1)
print(s2.minTimeToVisitAllPoints(case1))
print(case2)
print(s2.minTimeToVisitAllPoints(case2))