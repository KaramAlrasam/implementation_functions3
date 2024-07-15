a=[2,5,1,4,3,8,7,0,9]
def sortedSelction(m_list:list):
  #create variable has zero value
  start_p=0
  #create while loop 
  while start_p<len(m_list):
    #selct minumm item and its position 
    selct=m_list.index(min(m_list[start_p:]))
    #move minmmum item to the left 
    m_list[start_p],m_list[selct]=m_list[selct],m_list[start_p]
    #update start_p
    start_p+=1
  #return sorted list
  return m_list
print(sortedSelction(a))
a=[1,4,2,3,8,5,6,0,8,9,10]
def sortedSelction2(m_list):
  def minIndex(m_list):
    
    num=m_list[0]
    poss=0
    for i in range(len(m_list)):
      if m_list[i]<num:
        num=m_list[i]
        poss=i
    return poss
 
    
  for i in range(len(m_list)-1):
    m_min_ind=minIndex(m_list[i:])
    m_min_ind+=i
    m_list[m_min_ind], m_list[i]=m_list[i], m_list[m_min_ind]
  return m_list

print(sortedSelction2(a))

    