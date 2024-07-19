a=[1,4,2,3,7,5,6,0,8,9,10]
def QuickSort(m_list):
  #make condition baseCase if length of m_list==1 or lesser that's mean 
  #it's sorted
  if len(m_list)<=1:
    return m_list
  else:
    #find the mid of m_list by using this formila (len(m_list)//2)
    mid=len(m_list)//2
    #compersin m_list[mid] with lesser value and put its item in leftPartition
    leftPartition=[x for x in m_list if x<m_list[mid]]
    #compersin m_list[mid] with == value and put its item in middlPartition
    middlPartition=[x for x in m_list if x==m_list[mid]]
    #compersin m_list[mid] with greader value and put its item in RightlPartition
    RightlPartition=[x for x in m_list if x>m_list[mid]]
    #conctenate left+middle+right and use ricursive to repete this operation multi times
    return QuickSort(leftPartition) + middlPartition + QuickSort(RightlPartition)

print(QuickSort(a))
