import heapq
# from functools import reduce 
num1 = [[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15]]
def find_kth_smallest(mat, k):
  #get the length of the row and of the column
  m, n=len(mat), len(mat[0])
  #build another one heas False content
  temp=[[False]*n for _ in range(m)]
  #creat list has tuple, each tuple represent the element in mat and its position in mat
  q=[(mat[0][0], 0, 0)]
  #create variable will be the result of output
  ans=None
  #update the first element in temp and convert it into True
  temp[0][0]=True
  #create for loop and using k
  for _ in range(k):
    #update ane and its position
    ans, i, j=heapq.heappop(q)
    if i+1 < m and not temp[i+1][j]:
      #that's mean, it had been added
      temp[i+1][j]=True
      heapq.heappush(q, (mat[i+1][j], i+1, j))
    if j+1 < n and not temp[i][j+1]:
      temp[i][j+1]=True
      heapq.heappush(q,(mat[i][j+1], i, j+1))
  return ans

print(find_kth_smallest(num1, 11))
      
  


    
  


    
    



  
  

  
    
    
  
