class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # limits
        top =0
        bottom= len(matrix) -1 # size m
        left= 0
        right= len(matrix[0]) -1 #size n
        results= []
        
        while top<=bottom and left<=right:
            #move to the right
            for i in range(left, right+1):
                results.append(matrix[top][i])
            top+=1
            
            #move down
            for i in range(top, bottom+1):
                results.append(matrix[i][right])
            right -=1
            
            #move to the left
            if top <=bottom:
                for i in range(right, left-1, -1):
                    results.append(matrix[bottom][i])
                bottom-=1
            
            #move up
            if left<= right:
                for i in range(bottom, top-1, -1):
                    results.append(matrix[i][left])
                left +=1
            
        return results
        
case1= [[1,2,3],[4,5,6],[7,8,9]]
case2= [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
s= Solution()
print(case1)
print(s.spiralOrder(case1))
print(case2)
print(s.spiralOrder(case2))

# NOTES
#m == matrix.length
#n == matrix[i].length
# first: move from matrix[0][0]till matrix[0][n]
# second: move from matrix[0][n] all the way to matrix[m][n]
# third: move from matrix[m][n] all the way to matrix[m][0]
# fourth: move from matrix[m][0] all the way to matrix[1][0]
# final: move from matrix[1][0] all the way to matrix[1][n]