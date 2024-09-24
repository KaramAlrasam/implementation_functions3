import heapq
from collections import Counter
par="aab"
def fre_letters(m_str):
    #count friquintly letters
    ctr=Counter(m_str)
    # convert ctr into list with tuples
    heap=[(-ctr[l], l)for l in ctr]
    # buld heab by using heapify
    heapq.heapify(heap)
    # create two variables one to count letters and another for letters
    prev_count, prev_letter=0, ""
    # create empty list as result for display
    res=[]
    #create while loop on the heap
    while heap:
        #pop heap
        count, letter=heapq.heappop(heap)
        # append letter to res
        res.append(letter)
        #create condition for prives letters
        if prev_count < 0:
            heapq.heappush(heap, (prev_count, prev_letter))
        prev_count, prev_letter= count+1, letter
    if len(res) == len(m_str):
        return "".join(res)
             
        
    
    


    
    
    
print(fre_letters(par))   
        
