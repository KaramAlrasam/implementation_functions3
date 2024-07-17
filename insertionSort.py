a=[2,4,1,3,7,5,6,0,8,9]
def insertionSort(m_list:list)->list:
  for i in range(1,len(m_list)):
    for j in range(i-1,-1,-1):
      if m_list[j]>m_list[j+1]:
        m_list[j],m_list[j+1]=m_list[j+1],m_list[j]
      else:
        break
  return m_list
print(insertionSort(a))


b=[2,4,1,3,7,5,6,0,8,9]
def insertionSort2(m_list:list):
  for i in range(1,len(m_list)):
    j=i-1
    while m_list[j]>m_list[j+1] and j>=0:
      m_list[j],m_list[j+1]=m_list[j+1],m_list[j]
      j-=1
  return m_list

print(insertionSort2(b))