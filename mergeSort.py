

a=[1,4,2,6,3,7,5,9,8,0]
def mergeSort(m_list:list)->list:
  #make condition to find out the size of the list
  if len(m_list)>1:
    #find the middle of m_list by this fomila (len(m_list))//2
    mid=len(m_list)//2
    #create two Array left and right by dividing m_list and using mid
    Ar1=m_list[:mid]
    Ar2=m_list[mid:]
    #repete this operation multi times by using recursive
    mergeSort(Ar1)
    mergeSort(Ar2)
    #create three variables and update them later
    k=i=j=0
    #after you divided, conquer now
    while i<len(Ar1)and j<len(Ar2):
      if Ar1[i]<=Ar2[j]:
        m_list[k]=Ar1[i]
        i+=1
      else:
        m_list[k]=Ar2[j]
        j+=1
      k+=1
    #merge thr reminder of the items in Ar1 & Ar2 to m_list
    while i<len(Ar1):
      m_list[k]=Ar1[i]
      i+=1
      k+=1
    while j<len(Ar2):
      m_list[k]=Ar2[j]
      j+=1
      k+=1
    return m_list
print(mergeSort(a))      
    
    
