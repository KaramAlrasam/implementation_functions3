import heapq
from collections import Counter
par=[4,1,3,2,9,6,7,8,0,10,11,12]
def mid_number(numbers):
    if not numbers:
        return
    max_heap=[]
    min_heap=[]
    heapq.heappush(max_heap, -numbers[0])
    for i in range(1, len(numbers)):
        num=numbers[i]
        if num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)
        if len(max_heap) > len(min_heap)+1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
    if len(max_heap) > len(min_heap):
        return -max_heap[0]
    else:
        return (-max_heap[0] + min_heap[0])/2
            
    

        
        
            
            
            
    
     
    
    
    
print(mid_number(par)) 
